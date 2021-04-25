<template>
  <v-container>
    <v-row align="center" justify="center">
      <!-- <div id="app"> -->
      <v-col cols="12">
        <h2 class="display-2 m-3 text-center">View Ratings of Professors</h2>
      </v-col>

      <v-col cols="6">
        <section v-if="errored">
          <p>
            We're sorry, we're not able to retrieve this information at the
            moment, please try back later
          </p>
        </section>

        <section v-else>
          <div v-if="loading">Loading...</div>

          <div v-else>
            <v-simple-table>
              <template v-slot:default>
                <thead>
                  <tr>
                    <th>Professor Code</th>
                    <th>Rating</th>
                  </tr>
                </thead>
                <tbody>
                  <tr :key="idx" v-for="(data, idx) in info">
                    <td>{{ data.code }}</td>
                    <td>{{ data.rating }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
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
      // info: [],
      info: null,
      loading: true,
      errored: false,
    };
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/view/")
      .then((response) => (this.info = response.data.rating_list))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
}; // export defualt
</script>

<style>
</style>