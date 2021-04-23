#ping_main.py
#功能: 由使用者輸入CIDR網段，進行範圍內IP掃描並列印出有回應的IP及對應的MAC號
import module.GetIpList  #查詢CIDR網段中的所有IP
import module.PingIp  #ping出範圍內有回應的IP
import module.Get_mac    #針對有回應的IP找對應MAC號


#主程序
if __name__ == "__main__":
    ipList = GetIpList()
    #print("掃瞄範圍內的所有IP:",result)

    pingResultList = PingIp(ipList)
    #print("有回應的IP:", result)

    macResultList= module.Get_mac.GetMac(pingResultList)
    #print("對應的MAC號:", result)

    Output(ipList, pingResultList, macResultList)
    #print("印出所有OutPut:", result)



