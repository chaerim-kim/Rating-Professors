<template>
  <div>
    <navbar />
    <main>
      <section class="relative w-full h-full py-40 min-h-screen">
        <router-view />
        <!-- <footer-small absolute /> -->
      </section>
    </main>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";

export default {
  data() {
    return {
    //   registerBg2,
    };
  },
  components: {
    Navbar,
    // FooterSmall,
  },
};
</script>