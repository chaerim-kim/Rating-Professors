<template>
  <v-container>
    <v-row>
      <v-flex>
        <v-col cols="12">
          <!-- margin by 3 all sides -->
          <h2 class="display-2 m-3 text-center">Login</h2>
          <p class="text-xs-center">
            <router-link :to="{ name: 'register' }">
              Need to Register?
            </router-link>
          </p>
          <form>
            <v-text-field v-model="username" label="ID"> </v-text-field>

            <v-text-field v-model="password" type="password" label="Password">
            </v-text-field>

            <v-btn class="mr-4" @click="login()"> Login </v-btn>
          </form>
          <p>{{ flashMessage }}</p>
        </v-col>
      </v-flex>
    </v-row>
  </v-container>
</template>


<script>
import axios from "axios";

export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",
      loading: true,
      errored: false,
      flashMessage: "",
    };
  },

  methods: {
    login() {
      // console.log(this.username, this.password);
      axios
        .post("http://127.0.0.1:8000/api/login/", {
          username: this.username,
          password: this.password,
        })
        // .then(function (response) {
        //   console.log(response);
        // })
        .then((response) => (this.flashMessage = response.data))

        .catch(function (error) {
          console.log(error);
        });
    },
  }, //methods
}; //export
</script>

<style>
</style>