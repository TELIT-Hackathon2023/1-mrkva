<template>
    <div id="report">
      <header>
        <h1>Lighthouse Report</h1>
        <p>Website: <strong>{{ reportData.website }}</strong></p>
      </header>
  
      <section class="scores">
        <div class="score" v-for="(value, key) in reportData.scores" :key="key">
          <h2>{{ key }}</h2>
          <p>{{ value }}</p>
        </div>
      </section>
  
      <section class="details">
        <div v-for="(detail, name) in reportData.details" :key="name">
          <h3>{{ name }}</h3>
          <ul>
            <li v-for="(value, key) in detail" :key="key">
              {{ key }}: {{ value }}
            </li>
          </ul>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LighthouseReport',
    data() {
      return {
        reportData: {
          website: 'https://example.com',
          scores: {
            Performance: '90',
            Accessibility: '95',
            BestPractices: '88',
            SEO: '92',
          },
          details: {
            'First Contentful Paint': {
              Value: '2.0s',
              Score: '95'
            },
            'Speed Index': {
              Value: '4.1s',
              Score: '89'
            },
            // Add more details as needed
          }
        }
      };
    }
  }
  </script>
  
  <style scoped>
  #report {
    font-family: Arial, sans-serif;
    margin: 20px;
  }
  
  header {
    background-color: #f4f4f4;
    padding: 15px;
    text-align: center;
  }
  
  .scores {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  .score {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    width: 20%;
    text-align: center;
  }
  
  .details {
    margin-top: 20px;
  }
  
  h1, h2, h3 {
    color: #333;
  }
  </style>
  