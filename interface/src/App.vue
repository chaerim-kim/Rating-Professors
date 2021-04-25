<template>
  <div id="app">
    <!-- 헤더는 안바뀌고 밑부분만 재로딩됨 -->
    <Navbar /> 
    <!-- <div id="content" class="content">
      <router-view></router-view>
    </div> -->
  </div>
</template>

<script>
// import Header from './components/layout/Header.vue';
import Navbar from './components/layout/Navbar.vue';

// 가꼬와서 넣어줘야됨
export default {
  name: 'App',
  components: {
    Navbar,
  },

  data: () => ({
    //
  }),
};
</script>
