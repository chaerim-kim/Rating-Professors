<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="my-5">
        <v-img
          :src="require('../assets/RMP.png')"
          class="my-1"
          contain
          height="71"
        />
      </v-col>

      <v-col class="mt-4">
        <h3 class="text-center">Enter your <b>school</b> to get started</h3>
      </v-col>

      <v-col cols="12" class="mt-3">
        <v-text-field
          label="  Your School"
          prepend-inner-icon="mdi-school-outline"
          filled
          hide-details="auto"
          rounded
          dense
        ></v-text-field>
      </v-col>

      <v-col class="p-0">
        <p class="text-center">I'd like to look up a professor by name</p>
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
export default {};
</script>


<style scoped>
.head {
  margin-top: 120px;
}
</style>