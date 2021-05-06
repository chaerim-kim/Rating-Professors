<template>
  <v-container>
    <v-row align="center" justify="center">
        <v-col cols="8">
        <!-- margin by 3 all sides -->
        <h2 class="display-2 m-3 text-center">Sign up</h2>
        <!-- </v-col> -->

        <!-- <v-col cols="6" align="center"> -->
            <p class="text-xs-center">
                <router-link :to="{ name: 'login' }"> Have an account? </router-link>
            </p>

            <form>
                <v-text-field v-model="username" label="ID"></v-text-field>
                <v-text-field v-model="email" label="Email"></v-text-field>
                <v-text-field v-model="password" label="Password"></v-text-field>
                <v-btn class="mr-4" @click="submit"> Sign up </v-btn>
            </form>
        </v-col>
    </v-row>
  </v-container>
</template>


<script>
// import axios from 'axios'

export default {
    // // name of the component
    // name: 'register',

    // mounted(){
    //     axios({
    //         method: "GET",
    //         "url": 'http://127.0.0.1:8000/api/login/'
    //     }).then(response => console.log(response));
        
 
    // },

    // data: {

    // }

};


</script>

<style>
</style>