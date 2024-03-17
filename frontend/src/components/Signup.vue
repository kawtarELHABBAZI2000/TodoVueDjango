<template>
    <div class="container">
        <div class="row py-4 flex-column d-flex-align-items-center justify-content-center middle-content">
            <div class="col-md-8">
                <h3 class="text-muted text-start text-monospace">
                    Create your account
                </h3>
                <hr>
                <form @submit.prevent="submitForm">
                    <div v-if="errors.wrong_credentials" class="form-group my-2 text-start">
                        <small class="text-danger">{{ errors.wrong_credentials }}</small>
                    </div>
                    <div class="form-group my-2 text-start">
                       <input class="form-control" type="username" placeholder="Enter your username" name="username" autocomplete="username" v-model="username">
                       <small v-if="errors.username" class="text-danger">{{ errors.username }}</small>
                    </div>
                    <div class="form-group my-2 text-start">
                       <input class="form-control" type="password" placeholder="Enter your password" name="password" autocomplete="password" v-model="password">
                       <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
                    </div>
                    <div class="form-group my-2 text-start">
                       <input class="form-control" type="password" placeholder="Enter your password" name="password" autocomplete="password2" v-model="password2">
                       <small v-if="errors.password2" class="text-danger">{{ errors.password2 }}</small>
                    </div>
                    <div class="form-group my-2 d-grid gap-2">
                        <button class="btn btn-primary">
                            Signup to the system
                        </button>
                    </div>
                    <div class="form-group text-start my-2 d-grid gap-2">
                        <p>
                            Already have an account in the system. 
                            <router-link class="text-decoration-none" to="/">Click</router-link> here to login !
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>


</template>

<script>
import axios from 'axios';

export default {
  name: 'Signup',
  data() {
    return {
        username: "",
        password: "",
        password2: "",
        errors: {
            username: "",
            password: "",
            password2: "",
            wrong_credentials: ""
        }
    }
  },
  methods: {
    isValidForm(){
        let valid = true;
        if(!this.username){
            this.errors.username = "The field cannot be blank";
        }
        else{
            this.errors.username = "";
        }
        if(!this.password){
            this.errors.password = "The field cannot be blank";
        }
        else{
            this.errors.password = "";
        }
        if(this.password && this.password2 && this.password != this.password2){
            this.errors.password2 = "Password mismatched";
        }
        else{
            this.errors.password2 = "";
        }
        if(this.errors.username || this.errors.password || this.errors.password2){
            valid = false;
        }
        return valid;
    },
    submitForm() {
        if (this.isValidForm()) {
            const url = '/auth/users/';
            axios.post(url, {username: this.username, password: this.password})
                .then(response => {
                    this.$router.push('/');
                    console.log(response.data);
                    this.username = "";
                    this.password = "";
                    this.password2 = "";
                })
                .catch(error => {
                    console.log(error.response.data);
                    if(error.response.data.username){
                        this.errors.username = error.response.data.username.join('');
                    }
                    else{
                        this.errors.username = "";
                    }
                });
        }
    }

}
}
</script>

<style scoped lang="scss">

    .middle-content{
        height: 100vh;
    }

</style>
