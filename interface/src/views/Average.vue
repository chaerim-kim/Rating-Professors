<template>
  <v-container>
    <v-row>
      <!-- <div id="app"> -->
        <v-col cols="12">
          <h2 class="display-2 m-3 text-center">Average Rating</h2>
        </v-col>

        <v-col>
          <section v-if="errored">
            <p>
              We're sorry, we're not able to retrieve this information at the
              moment, please try back later
            </p>
          </section>

          <section v-else>
            <!-- <div v-if="loading">Loading...</div> -->

            <div >
              <form>
                <v-text-field v-model="form.professor_id" label="Professor ID">
                </v-text-field>

                <v-text-field v-model="form.module_code" label="Module Code">
                </v-text-field>

                <v-btn class="mr-4" @click="submit()"> Submit </v-btn>
              </form>
              <p>{{ flashMessage }}</p>
            </div>
          </section>
        </v-col>
      <!-- </div> -->
    </v-row>
  </v-container>
</template>


<script>
import axios from "axios";

export default {
  // name of the component
  name: "list",

  data() {
    return {
      flashMessage: "",
    //   loading: true,
      errored: false,
      
      form: {
        professor_id: "",
        module_code: "",
      },
    };
  },

  methods: {
    submit() {
      console.log(this.form);
      axios
        .post("http://127.0.0.1:8000/api/average/", this.form)
        .then((response) => (this.flashMessage = response.data))
        // .then((res) => {
        //     console.log(res.data);
        // })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    }, //submit
  }, // methods
}; //export degault
</script>

<style>
</style>