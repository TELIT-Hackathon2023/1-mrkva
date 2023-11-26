<template>
  <v-card color="white" flat height="1000px" rounded="0">
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

    <section class="score-section">
      <div class="score-container">
        <h1>Score</h1>
        <div class="score-value">
          <h3>{{ scoreValue }} / 10</h3>
        </div>
      </div>
    </section>

    <section class="personas-section">
      <div class="personas-container">
        <h2>Personas</h2>
        <div class="personas-cards">
          <v-card v-for="persona in personas" :key="persona.type" class="persona-card">
            <strong>{{ persona.type }}:</strong> {{ persona.interests }}
          </v-card>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="text-container">
        <div class="summary-container">
          SUMMARY
          <ul class="lists">
            <li>{{ summary }}</li>
          </ul>
        </div>

        <div class="improvements-container">
          IMPROVEMENTS
          <ul class="lists">
            <li v-for="improvement in improvementsPoints" :key="improvement">
              {{ improvement }}
            </li>
          </ul>
        </div>
      </div>

      <div class="image-container">
  <img src="@/assets/logoIQ.png" alt="Descriptive Alt Text" />
</div>

    </section>

  </v-card>
  <footer class="footer">
    <p>© 2023</p>
  </footer>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      summary: '',
      improvementsPoints: [],
      personas: [],
      scoreValue: 0,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:8000/myapp/test-api/?url=https://gymbeam.sk/')
        .then(response => {
          this.scoreValue = response.data.ux_score;
          this.summary = response.data.summary;
          this.improvementsPoints = response.data.improvements.map(improvement => `${improvement.area}: ${improvement.suggestion}`);
          this.personas = response.data.personas;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
}
</script>

<style scoped>
  .v-app-bar-nav-icon {
    padding-left: 10px;
  }

  .v-toolbar-title {
    padding-left: 20px;
  }

  .cards-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap; /* Ensures responsiveness */
    padding-left: 80px;
    padding-right: 80px;
    padding-top: 20px;
    padding-bottom: 30px;
  }

  @media (max-width: 600px) {
    .card-container {
      flex-direction: column;
    }
  }

  #app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: white; /* Dark background */
  }

  .lists {
    padding: 0 90px;
  }

  .search-wrapper {
    width: 100%; /* Take full width */
    height: 100%; /* Take full height */
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

  .score-container {
    text-align: center; /* Center the text */
    font-size: 20px; /* Adjust the font size as needed */
    padding-bottom: 20px;
  }

  .score-container {
    text-align: center; /* Center the text */
    font-size: 20px; /* Adjust the font size as needed */
    padding-top: 20px; /* Adjust padding to fit under the pink header */
    background: #fff; /* Same as v-card color */
  }

  .personas-section h2 {
    text-align: center;
  }

  .personas-cards {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }

  .persona-card {
    width: 20%;
    text-align: center;
    padding: 10px;
    margin: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }

  .content-section {
    display: flex;
    justify-content: space-around;
    padding: 0 50px;
  }

  .text-container {
    width: 50%; /* Adjusted width */
  }

  .summary-container, .improvements-container {
    font-size: 1em; /* Smaller font size */
  }

  .image-container {
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .image-container img {
    max-width: 80%;
    height: auto;
  }

  @media (max-width: 768px) {
    .personas-cards {
      flex-direction: column;
    }

    .persona-card {
      width: 100%;
      margin-bottom: 10px;
    }

    .content-section {
      flex-direction: column;
      padding: 0 20px;
    }

    .text-container, .image-container {
      width: 100%;
    }
  }

  .footer {
    background-color: #E91E63;
    color: white;
    text-align: center;
    padding: 10px 0;
    left: 0;
    bottom: 0;
    width: 100%;
  }
</style>
