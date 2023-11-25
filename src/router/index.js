import { createWebHistory, createRouter } from "vue-router";
import InputUrlPage from "@/views/InputUrlPage.vue";
import DetailReportPage from "@/views/DetailReportPage.vue";



const routes = [
  {
    path: "/",
    name: "InputUrlPage",
    component: InputUrlPage,
  },
  {
    path: "/detail",
    name: "DetailReportPage",
    component: DetailReportPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
