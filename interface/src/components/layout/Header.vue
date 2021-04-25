<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <!-- <b-nav-item href="#">Login</b-nav-item> -->
        <b-nav-item href="/list">List</b-nav-item>
        <b-nav-item href="/view">View</b-nav-item>
        <b-nav-item href="#">Average</b-nav-item>
        <b-nav-item href="/rate">Rate</b-nav-item>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="/register">Register</b-dropdown-item>
          <b-dropdown-item href="/login">Login</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>


<script>
  export default{
    name:"header",
  };
</script>


