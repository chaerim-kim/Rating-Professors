<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="grey" dark elevation="0">
        <!-- 토글역할. 누르면 sidebarmenu boolean 을 negate해서 보여주소 안보여주고 -->
        <v-app-bar-nav-icon
          @click="sidebarMenu = !sidebarMenu"
        ></v-app-bar-nav-icon>
        <v-spacer></v-spacer>
        
        <v-icon @click="$router.push( '/login')">mdi-account-plus</v-icon>
        <v-icon @click="$router.push( '/register')">mdi-login</v-icon>
      </v-app-bar>

      <v-navigation-drawer v-model="sidebarMenu" app floating>
        <v-list dense nav>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            @click="$router.push({ path: item.route })"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <v-container fluid>
          <v-row class="fill-height">
            <v-col>
              <transition name="fade">
                <router-view></router-view>
              </transition>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
      <!-- <v-footer> Chae Rim Kim </v-footer> -->
    </v-app>
  </div>
</template>



<script>
// 가꼬와서 넣어줘야됨
export default {
  data() {
    return {
      sidebarMenu: false,
      items: [
        { title: "Home", icon: "mdi-view-dashboard", route: "/" },
        { title: "List", icon: "mdi-view-dashboard", route: "/list" },
        { title: "View", icon: "mdi-image", route: "/view" },
        { title: "Average", icon: "mdi-help-box", route: "/average" },
        { title: "Rate", icon: "mdi-help-box", route: "/rate" },
      ],
      right: null,
    };
  },
};
</script>

<style scoped>
</style>