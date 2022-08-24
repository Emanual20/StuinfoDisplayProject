<template>
  <div class="home">
    <Header />
    <div class="container">
      <p class="lead">
        登陆前请阅读如下注意事项，感谢！
      </p>
      <ul class="list-unstyled">
        <li>
          登录相关:
          <ul>
            <li>
              默认用户名为中文姓名，密码为身份证号，最后一位为X的输入大写X。<b
                >强烈建议您在第一次登录后修改默认密码。</b
              >
            </li>
            <li><b>新增了注册功能，但是暂时不公开开放。2022.8.7</b></li>
            <li><b>新增了修改密码功能。2022.8.8</b></li>
            <li>
              <b>新增了查看个人信息功能，登陆后点击自己姓名即可。2022.8.23</b>
            </li>
            <li><b>新增了吐槽版功能。2022.8.24</b></li>
          </ul>
        </li>
        <li>
          功能相关:
          <ul>
            <li>
              登录后<b>强烈建议您</b>先更新自己信息，再设置其他同学查看您<b>详细</b>毕业去向的权限，以便其他同学查看信息。
            </li>
            <li>
              登录后您可以查看所有向您开放信息权限用户的详细信息，如毕业去向。未被开放查看详细毕业去向信息的同学只能看到模糊毕业去向。如：被查看同学A的毕业去向为"斯坦福大学计算机专业博士"，同学B未获得同学A的毕业去向查看信息，只能查看到信息"国外升学"。
            </li>
          </ul>
        </li>
        <li>
          Bug反馈相关：
          <ul>
            <li>
              由于制作时间短，且本人前后端制作水平有限，本网站可能存在或多或少的bug。
            </li>
            <li>
              请千万不要做SQL注入等安全测试、DDOS等压力测试，避免服务器和服务宕机。
            </li>
            <li>
              您可以随时通过微信或<a href="mailto:emanual20@foxmail.com">邮件</a
              >联系的方式向我反馈bug。
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
    onMounted(() => {
      console.log(context.root.$route.path);
    });
  }
};
</script>
