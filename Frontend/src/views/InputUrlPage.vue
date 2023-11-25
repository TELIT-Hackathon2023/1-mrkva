<template>
  <v-card color="white" flat height="200px" rounded="0">
    <v-toolbar color="pink" density="compact">
      <v-app-bar-nav-icon>
        <img src="@/assets/tsystems2.png" alt="T-Systems Logo" style="height: 30px; width: 30px;"/>
      </v-app-bar-nav-icon>

      <v-toolbar-title>UX Analyzer</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
  </v-card>
  
  <img src="@/assets/logoIQ.png" alt="T-Systems Logo" style="height: 30px; width: 30px;"/>
  
</template>
  
  <script>
  export default {
    name: 'GoogleMainPage'
    // Add your component logic here
  }
  </script>
  
  <style scoped>
  #app {
    text-align: center;
  }
  
  .top-bar {
    background-color: #e20074; /* Telecom magenta color */
    padding: 10px;
    text-align: left;
  }
  
  .logo {
    width: 100px; /* Adjust as needed */
    height: auto;
  }
  
  .main-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  .search-input {
    width: 60%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
  }
  </style>
  