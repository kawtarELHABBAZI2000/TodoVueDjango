<template>
    <div class="container">
        <div class="row py-4 flex-column d-flex-align-items-center justify-content-center middle-content">
            <div class="col-md-8">
                <h3 class="text-muted text-start text-monospace">
                    Login to your account
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
                    <div class="form-group my-2 d-grid gap-2">
                        <button type="submit" class="btn btn-primary">
                            Login to the system
                        </button>
                    </div>
                    <div class="form-group text-start my-2 d-grid gap-2">
                        <p>
                            Don't have an account in the system. Please
                            <router-link class="text-decoration-none" to="/signup">Click</router-link> to register !
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
  name: 'Login',
  data() {
    return {
        username: "",
        password: "",
        errors: {
            username: "",
            password: "",
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
        if(this.errors.username || this.errors.password){
            valid = false;
        }
        return valid;
    },
    submitForm() {
        if (this.isValidForm) {
            const url = '/login/';
            axios.post(url, {username: this.username, password: this.password})
                .then(response => {
                    this.$store.commit('setToken', response.data);
                    this.username = "";
                    this.password = "";
                    this.$router.push('/todo');
                })
                .catch(error => {
                    if (error.response.data.non_field_errors) {
                        this.errors.wrong_credentials = error.response.data.non_field_errors.join('');
                    } else {
                        this.errors.wrong_credentials = "";
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
