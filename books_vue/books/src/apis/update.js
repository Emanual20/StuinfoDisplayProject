import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function UpdateInfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            infos: postParams.infos,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function UpdatePermPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            stu_uuid: postParams.stu_uuid,
            allpermvalue: postParams.allpermvalue,
            infos: postParams.infos,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}