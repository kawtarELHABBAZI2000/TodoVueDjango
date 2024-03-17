<template>
    <div class="container">
        <div class="row py-4 d-flex flex-column align-items-center justify-content-center middle-content">
            <div class="col-md-12 my-4">
                <form v-if="!editing.status" @submit.prevent="addNew" class="d-flex flex-row" action="" method="POST">
                    <input class="form-control" type="text" name="title" placeholder="What do you wanna do today ?" v-model="newItem.title" required/>
                    <button class="btn ms-2 btn-primary">Add</button>
                </form>
                <form v-else @submit.prevent="update" class="d-flex flex-row" action="" method="POST">
                    <input class="form-control" type="text" name="title" placeholder="What do you wanna do today ?" v-model="editing.item.title" required/>
                    <button class="btn ms-2 btn-primary">Update</button>
                </form>
            </div>
            <div class="col-md-12 text-start">
                <table class="table">
                    <thead>
                        <tr>
                        <th scope="col"></th>
                        <th scope="col"></th>
                        <th scope="col"></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for = "item in todos" v-bind:key = "item.id">
                        <td :class="{ 'completed-task': item.completed }">{{ item.title }}</td>
                        <td>
                            <div class="form-check" v-if="item.completed">
                                <input class="form-check-input" type="checkbox" checked :id="item.id"  @change="changeStatus(item)">
                            </div>
                            <div v-else class="form-check">
                                <input class="form-check-input" type="checkbox" :id="item.id" @change="changeStatus(item)">
                            </div>
                        </td>
                        <td>
                            <svg @click="edit(item)" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square me-1" viewBox="0 0 16 16">
                                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                            </svg>

                            <svg @click="removeItem(item.id)" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                                <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                            </svg>
                        </td>
                        </tr>
                    </tbody>
                    </table>
            </div>
            <div class="col-md-12">
                <div class="form-group my-2 d-grid gap-2">
                    <button @click="logout" type="submit" class="btn btn-primary">
                        Logout of the system
                    </button>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import axios from 'axios';

export default {
  name: 'TodoList',
  data() {
    return{
        todos: [],
        newItem: {
            title: "",
            completed: false,
            user: this.$store.state.user_id
        },
        editing:{
            status: false,
            item: {}
        }
    }
    },
    methods: {
    fetchTodoList() {
        axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
        const url = '/list-create-todo/';
        axios.get(url)
            .then(response => {
                this.todos = response.data;
            })
            .catch(error => {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {
                    // The request was made but no response was received
                    console.log(error.request);
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log('Error', error.message);
                }
                console.log(error.config);
            });
    },
    addNew(){
        axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
        const url = '/list-create-todo/';
        axios.post(url, this.newItem)
        .then(response => {
            this.todos.unshift(response.data);
            this.newItem = {title: "", completed: false, user: this.$store.state.user_id};
        })
        .catch(error => {
            console.log(error);   
        })
    },
    edit(item){
        this.editing.status = true;
        this.editing.item = item;
        console.log(item)
    },
    changeStatus(item){
        this.editing.item = item;
        console.log(this.editing.item);
        this.editing.item.completed = !item.completed;
        this.update();
    },
    update(){
        axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
        const url = '/retrieve-update-destroy-todo/' + this.editing.item.id + '/';
        axios.put(url, this.editing.item)
        .then(response => {
            this.editing.status = false;
            this.editing.item = {};
            this.fetchTodoList(); 
        })
        .catch(error => {
            console.log(error);   
        })
    },
    removeItem(id){
        axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
        const url = '/retrieve-update-destroy-todo/' + id + '/';
        axios.delete(url)
        .then(response => {
            this.fetchTodoList();
        })
        .catch(error => {
            console.log(error);   
        })
    },
    logout(){
        this.$store.commit('removeToken');
        this.$router.push('/')
    }
},
    mounted() {
        this.fetchTodoList();
    }
}

</script>

<style scoped lang="scss">

    svg {
        cursor: pointer !important;
    }
    .middle-content{
        height: 100vh;
    }
    .completed-task {
    text-decoration: line-through;
    }

</style>
