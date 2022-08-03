import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function GetInfo(){
    return service.request({
        method: "get",
        url: "/user_stuinfos"
    })
};

export function GetInfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            key: postParams.key, // newest 
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos') // 预留字段给加密用
        }
    })
}

export function CheckPwPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            password: postParams.password,
            key: postParams.key, // newest
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function FetchAdmittedInfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            key: postParams.key, // newest 
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos') // 预留字段给加密用
        }
    })
}