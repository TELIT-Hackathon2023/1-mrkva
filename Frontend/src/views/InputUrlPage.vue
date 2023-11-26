<template>
  <v-card color="white" flat height="200px" rounded="0">
    <v-toolbar color="pink" density="compact">
      <v-app-bar-nav-icon>
        <img
          src="@/assets/tsystems2.png"
          alt="T-Systems Logo"
          style="height: 30px; width: 30px"
        />
      </v-app-bar-nav-icon>

      <v-toolbar-title>UX Analyzer</v-toolbar-title>

    </v-toolbar>
  </v-card>

  

  <div id="app">
    <div class="logo-container">
    <img src="@/assets/Component 1.png" alt="T-Systems Logo" class="logo" />
  </div>
    <div class="search-wrapper">
      <div class="search-container">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Insert url..."
          class="search-input"
        />
        <button class="search-button" @click="performSearch">Analyze</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GoogleMainPage",
  // Add your component logic here
};
</script>

<style scoped>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white; /* Dark background */
  flex-direction: column;
}

.search-wrapper {
  width: 100%; /* Take full width */
  display: flex; /* Use Flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
}

.search-container {
  display: flex;
  border: 1px solid #5f6368; /* Light grey border */
  border-radius: 24px;
  overflow: hidden;
}

.search-input {
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  color: white;
  background-color: transparent;
  outline: none;
  flex-grow: 1;
}

.search-input::placeholder {
  color: #9aa0a6; /* Placeholder text color */
}

.search-button {
  border: none;
  padding: 12px 24px;
  background-color: #5f6368; /* Light grey background */
  color: white;
  cursor: pointer;
  outline: none;
}

.search-button:hover {
  background-color: #3c4043; /* Slightly darker grey on hover */
}

.logo-container {
  padding-left: 95px;
}


</style>
