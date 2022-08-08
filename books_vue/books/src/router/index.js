import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import StuinfoView from "../views/StuinfoView.vue";
import SelfinfoView from "../views/SelfinfoView.vue";
import ManageInfoView from "../views/ManageInfoView.vue";
import ManagePermView from "../views/ManagePermView.vue";

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

  // 注册页面
  {
    path: "/register/",
    name: "RegisterView",
    component: RegisterView
  },

  // 学生信息详情页
  {
    path: "/stuinfo/",
    name: "Stuinfo",
    component: StuinfoView,
  },

  // 个人信息详情页
  {
    path: '/selfinfo/',
    name: "Selfinfo",
    component: SelfinfoView,
  },

  // 个人信息变更页面
  {
    path: "/manageinfo/",
    name: "Manageinfo",
    component: ManageInfoView,
  },

  // 权限管理变更页面
  {
    path: '/manageperm/',
    name: "Manageperm",
    component: ManagePermView,
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
