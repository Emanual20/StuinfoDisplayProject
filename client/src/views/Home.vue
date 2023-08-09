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
            <li><b>Recent: </b>开放高考去向地图预览功能（只支持国内地点），吐槽版；优化信息展出页面。</li>
            <li>新增注册（目前只对2018届一贯制同学开放）、修改密码、查看个人信息（登陆后点击自己姓名即可）。</li>
            <li>
              登录后强烈建议您先<b>更新自己信息</b>。
            </li>
            <li>
              登录后您可以查看所有向您开放信息权限用户带有姓名的详细信息，如毕业去向。未被开放查看详细毕业去向信息的同学只能看到脱敏去向，即不包括姓名。
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
