import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function UpdatePasswordPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      username: postParams.username,
      npassword: postParams.npassword,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function UpdateInfoPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      username: postParams.username,
      infos: postParams.infos,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function UpdatePermPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      username: postParams.username,
      stu_uuid: postParams.stu_uuid,
      allpermvalue: postParams.allpermvalue,
      infos: postParams.infos,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function UploadSpitslotPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      stu_uuid: postParams.stu_uuid,
      info: postParams.info,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function RegisterUserPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      emailaddress: postParams.emailaddress,
      username: postParams.username,
      password: postParams.password,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function DeleteUserAccountPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      stu_uuid: postParams.user_uuid,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}
