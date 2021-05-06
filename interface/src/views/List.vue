<template>
  <v-container>
    <v-row align="center" justify="center">
      <!-- <div id="app"> -->
      <v-col cols="12">
        <h2 class="display-2 m-3 text-center">List all items</h2>
      </v-col>

      <v-col>
        <section v-if="errored">
          <p>
            We're sorry, we're not able to retrieve this information at the
            moment, please try back later
          </p>
        </section>

        <section v-else>
          <div v-if="loading">Loading...</div>
<!-- https://bezkoder.com/vuetify-data-table-example/ -->
          <div v-else>
            <template >
              <v-data-table
                :headers="headers"
                :items="moduleinfo"
                :items-per-page="10"
                :search="search"

                :server-items-length="totalRatings"
              >
              <template v-slot:top>
                <v-text-field
                  v-model="search"
                  label="Search"
                  class="mx-4"
                ></v-text-field>
              </template>


                </v-data-table>
              </template>

            <!-- <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th>Module Code</th>
                      <th>Module Name</th>
                      <th>Year</th>
                      <th>Semester</th>
                      <th>Professor Code</th>
                      <th>Professor</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr :key="idx" v-for="(data, idx) in info">
                      <td>{{ data.module_code }}</td>
                      <td>{{ data.name }}</td>
                      <td>{{ data.year }}</td>
                      <td>{{ data.semester }}</td>
                      <td>{{ data.professor_id }}</td>
                      <td>{{ data.first_name + " " + data.last_name }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table> -->
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
      info: null,
      loading: true,
      errored: false,
      search: "",
      // totalRatings: 0,
      moduleinfo: [],
      headers: [
        { text: "Module Code", value: "module_code" },
        { text: "Module Name", value: "name" },
        { text: "Year", value: "year" },
        { text: "Semester", value: "semester" },
        { text: "Professor Code", value: "professor_id" },
        { text: "Professor First Name", value: "first_name" +"last_name" },
        { text: "Professor Name", value: "last_name" },
      ],
    };
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/list/")
      // .then((response) => (this.info = response.data.module_list))
      .then((response) => {
        this.moduleinfo = response.data.module_list;
      })

      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>

<style>
</style>