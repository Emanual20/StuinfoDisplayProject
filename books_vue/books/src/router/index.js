import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import LoginView from "../views/LoginView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import StuinfoView from "../views/StuinfoView.vue";
import ManageInfoView from "../views/ManageInfoView.vue";

Vue.use(VueRouter);

const routes = [
  // 网站首页
  {
    path: "/",
    name: "Home",
    component: Home
  },

  // 登陆页面
  {
    path: "/login/",
    name: "LoginView",
    component: LoginView
  },

  // 学生信息详情页
  {
    path: "/stuinfo/",
    name: "Stuinfo",
    component: StuinfoView,
  },

  // 个人信息变更页面
  {
    path: "/manageinfo/",
    name: "Manageinfo",
    component: ManageInfoView,
  },

  // 404 NotFoundPage
  {
    path: "/404/",
    name: "404",
    component: NotFoundView
  },

  {
    path: "/:catchAll(.*)",
    redirect: "/404/"
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
