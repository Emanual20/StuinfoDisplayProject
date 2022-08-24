import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function GetInfo() {
  return service.request({
    method: "get",
    url: "/user_stuinfos"
  });
}

export function GetStudents() {
  return service.request({
    method: "get",
    url: "/get_stuinfos"
  });
}

export function GetStudentsPermission(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      stu_uuid: postParams.stu_uuid,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function GetInfoPost(postParams) {
  return service.request({
    method: "post",
    url: "/fetchselfinfo",
    data: {
      stu_uuid: postParams.stu_uuid,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function CheckPwPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      username: postParams.username,
      password: postParams.password,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      )
    }
  });
}

export function FetchAdmittedInfoPost(postParams) {
  return service.request({
    method: "post",
    url: postParams.url,
    data: {
      username: postParams.username,
      key: postParams.key,
      secretKey: rsaEncrypt(
        new Date().getTime() + ":" + "www.baidu.com" + ":" + "otherinfos"
      ) // 预留字段给加密用
    }
  });
}
