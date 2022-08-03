<template>
  <div class="home">
    <Header />
    <div class="container">
      <p class="lead"> 
        This is a lead paragraph which you should notice before login.
      </p>
      <ul class="list-unstyled">
        <li>登录相关:
          <ul>
            <li>默认用户名为中文姓名，密码为身份证号，最后一位为X的输入大写X。</li>
            <li>暂时没有修改密码功能。</li>
          </ul>
        </li>
        <li>功能相关:
          <ul>
            <li>登录后请你<b>务必</b>先设置可以查看你自己<b>详细</b>毕业去向的用户，以便其他同学获取权限查看信息。</li>
            <li>登录后你可以查看所有向你开放信息权限用户的详细信息，如毕业去向。未被开放查看详细毕业去向信息的同学只能看到模糊毕业去向。如：被查看同学A的毕业去向为"斯坦福大学计算机专业博士"，同学B未获得同学A的毕业去向查看信息，只能查看到信息"国外升学"。</li>
          </ul>
        </li>
        <li>Bug反馈相关：
          <ul>
            <li>由于制作时间短，且本人前后端制作水平有限，本网站可能存在或多或少的bug。</li>
            <li>你可以随时通过微信或<a href="mailto:emanual20@foxmail.com">邮件</a>联系的方式向我反馈bug。</li>
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
import { GetInfoPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";


export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    onMounted(()=>{
      console.log(context.root.$route.path)
    });
  }

};
</script>