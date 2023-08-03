<template>
  <div class="home">
    <Header />
    <div class="container">
      <p class="lead">
        
      </p>
      <ul class="list-unstyled">
        <li>
          <b>登录</b>
          <ul>
            <li>
              默认用户名为中文姓名，密码为生日。如生日为1904.10.17，则默认密码为19041017。<b
                >强烈建议您在第一次登录后修改默认密码。</b
              >
            </li>
          </ul>
        </li>
        <li>
          <b>功能</b>
          <ul>
            <li>新增了注册（目前只对2018届六年一贯制同学开放）、修改密码、查看个人信息（登陆后点击自己姓名即可）、吐槽版功能。</li>
            <li>
              登录后强烈建议您先<b>更新自己信息</b>，再设置其他同学查看您详细毕业去向的权限。
            </li>
            <li>
              登录后您可以查看所有向您开放信息权限用户的详细信息，如毕业去向。未被开放查看详细毕业去向信息的同学只能看到模糊毕业去向。如：被查看同学A的毕业去向为"斯坦福大学计算机专业博士"，同学B未获得同学A的毕业去向查看信息，只能查看到信息"国外升学"。
            </li>
          </ul>
        </li>
        <li>
          <b>Bug反馈</b>
          <ul>
            <li>
              您可以随时通过<a href="mailto:emanual20@foxmail.com">邮件</a
              >反馈bug。
            </li>
          </ul>
        </li>
      </ul>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { ref, reactive, onMounted } from "@vue/composition-api";

export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
  }
};
</script>
