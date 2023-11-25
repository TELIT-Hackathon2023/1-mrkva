import { createWebHistory, createRouter } from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import strankyPage from "@/views/strankyPage.vue";



const routes = [
  {
    path: "/",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/stranky",
    name: "strankyPage",
    component: strankyPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
