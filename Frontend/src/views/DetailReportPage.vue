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
    <section>
      <div class="score-container">
        <h1>Score</h1>
        <div class="score-value">
          <h3>{{ scoreValue }} / 10</h3>
        </div>
      </div>
    </section>

    <section>
      <div class="cards-container">
        <v-card
          width="400"
          title="This is a title"
          subtitle="This is a subtitle"
          text="This is content"
        ></v-card>

        <v-card
          width="400"
          title="This is a title"
          subtitle="This is a subtitle"
          text="This is content"
        ></v-card>

        <v-card
          width="400"
          title="This is a title"
          subtitle="This is a subtitle"
          text="This is content"
        ></v-card>
      </div>
    </section>
    <section>
  <div class="summary-improvements-wrapper">
    <div class="text-container"> <!-- Renamed for clarity -->
      <div class="summary-container">
        SUMMARY
        <ul class="lists">
          <li v-for="point in summaryPoints" :key="point">{{ point }}</li>
        </ul>
        <!-- Additional content for SUMMARY can go here -->
      </div>

      <div class="improvements-container">
        IMPROVEMENTS
        <ul class="lists">
          <li v-for="point in improvementsPoints" :key="point">
            {{ point }}
          </li>
        </ul>
        <!-- Additional content for IMPROVEMENTS can go here -->
      </div>
    </div>

    <div class="image-container">
      <img src="@/assets/logoIQ.png" alt="Descriptive Alt Text" />
    </div>
  </div>
</section>
  </v-card>
  <footer class="footer">
    <p>© 2023</p>
  </footer>
  
</template>

<script>
export default {
  name: "LighthouseReport",
  data() {
    return {
      scoreValue: 5,
      summaryPoints: [],
      improvementsPoints: [],
      reportData: {
        website: "https://example.com",
        scores: {
          Performance: "90",
          Accessibility: "95",
          BestPractices: "88",
          SEO: "92",
        },
        details: {
          "First Contentful Paint": {
            Value: "2.0s",
            Score: "95",
          },
          "Speed Index": {
            Value: "4.1s",
            Score: "89",
          },
          // Add more details as needed
        },
      },
    };
  },
  mounted() {
    this.fetchDataFromAPI(); // Call the function when the component mounts
  },
  methods: {
    async fetchDataFromAPI() {
      // Placeholder for your API call
      const response = await fetch("url-to-your-api"); // Replace with your API URL
      const data = await response.json();
      this.summaryPoints = data.summary; // Assume your API returns a summary array
      this.improvementsPoints = data.improvements; // Assume your API returns an improvements array
    },
  },
};
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

.summary-improvements-wrapper {
  display: block; /* Change from flex to block to stack divs vertically */
  padding: 0 200px; /* Maintain the horizontal padding as needed */
}

/* Since they are no longer side by side, you can remove justify-content and align-items */
.summary-container,
.improvements-container {
  font-size: 1.5em; /* Keep font size consistent */
  margin: 20px 0; /* Add vertical margin for spacing */
}

/* You may want to adjust the responsive styles as well */
@media (max-width: 768px) {
  .summary-improvements-wrapper {
    padding: 0 20px; /* Adjust padding for smaller screens */
  }
  .summary-container,
  .improvements-container {
    font-size: 1.2em; /* Adjust font size for smaller screens */
    margin: 10px 0; /* Adjust vertical margin for smaller screens */
  }
}

section {
  border-bottom: 1px solid #e0e0e0; /* Light grey border for an aesthetic thin line */
  margin-bottom: 20px; /* Space after each section */
}

.summary-improvements-wrapper {
  display: flex;
  justify-content: space-between; /* This will space out the child divs */
  align-items: flex-start; /* Aligns items to the start of the cross axis */
  padding: 0 95px; /* Maintain the horizontal padding */
}

.text-container {
  flex: 1; /* Allows the container to grow and take up free space */
  display: flex;
  flex-direction: column; /* Stack summary and improvements vertically */
}

.image-container {
  flex-basis: 250px; /* Adjust the width of the image container */
  text-align: right; /* Align the image to the right */
}

@media (max-width: 768px) {
  .summary-improvements-wrapper {
    flex-direction: column; /* Stack elements vertically on smaller screens */
  }
  .text-container,
  .image-container {
    padding: 0 20px; /* Adjust padding for smaller screens */
  }
  .image-container {
    order: -1; /* This will move the image above the text on smaller screens */
  }
}

.footer {
  background-color:#E91E63;
  color: white;
  text-align: center;
  padding: 10px 0;
  
  left: 0;
  bottom: 0;
  width: 100%;
}
</style>
