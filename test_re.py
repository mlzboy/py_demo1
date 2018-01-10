#!/usr/bin/env python
#encoding=utf-8
import urllib2
import codecs
url = "http://www.zjhrss.gov.cn/col/col1389524/index.html"
html = urllib2.urlopen(url).read()
f = codecs.open("./html.txt","w","utf-8")
print "html type is:",type(html)
f.write(html.decode("utf-8","ignore"))
f.close()
html="""
<div id="4451525"><script type="text/xml"><datastore>
<nextgroup><![CDATA[<a href="/module/jpage/dataproxy.jsp?page=1&appid=1&appid=1&webid=2758&path=/&columnid=1389524&unitid=4451525&webname=浙江省人力资源和社会保障网&permissiontype=0"></a>]]></nextgroup>
<recordset>

<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/4/art_1389524_14812646.html' class='bt_link' title='新增7名国家“千人计划”青年项目人才 西湖区高层次人才集聚迈入快车道' target="_blank">新增7名国家“千人计划”青年项目人才 西湖区高层次人才集聚迈入快车道</a>  <span class='bt_time' style="float:right;">2018-01-04</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/4/art_1389524_14808204.html' class='bt_link' title='萧山区人力社保局“最多跑一次”再发力 惠民生顺民意贴民心' target="_blank">萧山区人力社保局“最多跑一次”再发力 惠民生顺民意贴民心</a>  <span class='bt_time' style="float:right;">2018-01-04</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/3/art_1389524_14775571.html' class='bt_link' title='高一截 长一头 胜一筹 象山县人力社保局全面锻造新时代人社干部队伍' target="_blank">高一截 长一头 胜一筹 象山县人力社保局全面锻造新时代人社干部队伍</a>  <span class='bt_time' style="float:right;">2018-01-03</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/3/art_1389524_14775523.html' class='bt_link' title='《丽水市全民医疗保险办法》顺利实施' target="_blank">《丽水市全民医疗保险办法》顺利实施</a>  <span class='bt_time' style="float:right;">2018-01-03</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/2/art_1389524_14753219.html' class='bt_link' title='台州市创新海外借才引智模式推动制造业转型升级' target="_blank">台州市创新海外借才引智模式推动制造业转型升级</a>  <span class='bt_time' style="float:right;">2018-01-02</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2018/1/2/art_1389524_14752866.html' class='bt_link' title='共识凝聚力量，思路指明方向——吴兴区人力社保局谋好2018人才工作新篇章' target="_blank">共识凝聚力量，思路指明方向——吴兴区人力社保局谋好2018人才工作新篇章</a>  <span class='bt_time' style="float:right;">2018-01-02</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/29/art_1389524_14738996.html' class='bt_link' title='省级结对帮扶青田团组成员单位赴青田开展扶贫工作调研' target="_blank">省级结对帮扶青田团组成员单位赴青田开展扶贫工作调研</a>  <span class='bt_time' style="float:right;">2017-12-29</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/28/art_1389524_14704127.html' class='bt_link' title='我省22起重大劳动保障违法行为公布' target="_blank">我省22起重大劳动保障违法行为公布</a>  <span class='bt_time' style="float:right;">2017-12-28</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/25/art_1389524_14576270.html' class='bt_link' title='全省“最美公务员”先进事迹报告会在杭州举行' target="_blank">全省“最美公务员”先进事迹报告会在杭州举行</a>  <span class='bt_time' style="float:right;">2017-12-25</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/25/art_1389524_14576267.html' class='bt_link' title='我省出台完善省属事业单位绩效工资政策若干意见' target="_blank">我省出台完善省属事业单位绩效工资政策若干意见</a>  <span class='bt_time' style="float:right;">2017-12-25</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/25/art_1389524_14564062.html' class='bt_link' title='浙皖开展家政服务劳务对接活动' target="_blank">浙皖开展家政服务劳务对接活动</a>  <span class='bt_time' style="float:right;">2017-12-25</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/25/art_1389524_14564058.html' class='bt_link' title='全省宣传贯彻《浙江省工伤保险条例》视频会在杭州召开' target="_blank">全省宣传贯彻《浙江省工伤保险条例》视频会在杭州召开</a>  <span class='bt_time' style="float:right;">2017-12-25</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/25/art_1389524_14564055.html' class='bt_link' title='2017年省直单位年度考核优秀年轻公务员能力提升培训班结业式在杭州举行' target="_blank">2017年省直单位年度考核优秀年轻公务员能力提升培训班结业式在杭州举行</a>  <span class='bt_time' style="float:right;">2017-12-25</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/22/art_1389524_14505844.html' class='bt_link' title='武义县强化纪检监督，助推社保服务效能新提升' target="_blank">武义县强化纪检监督，助推社保服务效能新提升</a>  <span class='bt_time' style="float:right;">2017-12-22</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/22/art_1389524_14505842.html' class='bt_link' title='金华市打造“IAM”模式助推农村电商发展' target="_blank">金华市打造“IAM”模式助推农村电商发展</a>  <span class='bt_time' style="float:right;">2017-12-22</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/21/art_1389524_14502389.html' class='bt_link' title='省厅召开全面推进“最多跑一次”改革第65次专题会议' target="_blank">省厅召开全面推进“最多跑一次”改革第65次专题会议</a>  <span class='bt_time' style="float:right;">2017-12-21</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/21/art_1389524_14502058.html' class='bt_link' title='2017年度省部属单位军队转业干部培训班在杭州举行' target="_blank">2017年度省部属单位军队转业干部培训班在杭州举行</a>  <span class='bt_time' style="float:right;">2017-12-21</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/20/art_1389524_14504941.html' class='bt_link' title='温州市人力社保局多措并举全力推动该市劳动人事争议仲裁与诉讼的有效对接' target="_blank">温州市人力社保局多措并举全力推动该市劳动人事争议仲裁与诉讼的有效对接</a>  <span class='bt_time' style="float:right;">2017-12-20</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/20/art_1389524_14504493.html' class='bt_link' title='桐庐县全力打造长期护理保险省级试点“桐庐样本”' target="_blank">桐庐县全力打造长期护理保险省级试点“桐庐样本”</a>  <span class='bt_time' style="float:right;">2017-12-20</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/20/art_1389524_14503396.html' class='bt_link' title='上虞区人力社保局以“三个抓”推进机关“大党建”' target="_blank">上虞区人力社保局以“三个抓”推进机关“大党建”</a>  <span class='bt_time' style="float:right;">2017-12-20</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/20/art_1389524_14502910.html' class='bt_link' title='立足自身优环境 接轨上海谋发展 面向全球聚英才——嘉兴人才工作迈入快车道' target="_blank">立足自身优环境 接轨上海谋发展 面向全球聚英才——嘉兴人才工作迈入快车道</a>  <span class='bt_time' style="float:right;">2017-12-20</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/19/art_1389524_14424673.html' class='bt_link' title='2018年浙江省各级机关单位考试录用公务员报名确认结束　缴费人数为27.70万人' target="_blank">2018年浙江省各级机关单位考试录用公务员报名确认结束　缴费人数为27.70万人</a>  <span class='bt_time' style="float:right;">2017-12-19</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/18/art_1389524_14372549.html' class='bt_link' title='我省出台劳动人事争议仲裁终局裁决适用规定' target="_blank">我省出台劳动人事争议仲裁终局裁决适用规定</a>  <span class='bt_time' style="float:right;">2017-12-18</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/14/art_1389524_14233112.html' class='bt_link' title='养老保险中心举办在杭中央属机关事业单位养老保险参保登记培训班' target="_blank">养老保险中心举办在杭中央属机关事业单位养老保险参保登记培训班</a>  <span class='bt_time' style="float:right;">2017-12-14</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/14/art_1389524_14233093.html' class='bt_link' title='全省劳动人事争议裁审衔接暨疑难案件研讨会在杭州召开' target="_blank">全省劳动人事争议裁审衔接暨疑难案件研讨会在杭州召开</a>  <span class='bt_time' style="float:right;">2017-12-14</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/13/art_1389524_14233086.html' class='bt_link' title='我省劳动人事争议裁审衔接工作先进经验获人社部肯定' target="_blank">我省劳动人事争议裁审衔接工作先进经验获人社部肯定</a>  <span class='bt_time' style="float:right;">2017-12-13</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/6/art_1389524_14233124.html' class='bt_link' title='绍兴深入推进“最多跑一次”改革取得新突破 实现人社业务“全市通办”' target="_blank">绍兴深入推进“最多跑一次”改革取得新突破 实现人社业务“全市通办”</a>  <span class='bt_time' style="float:right;">2017-12-06</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/5/art_1389524_14233078.html' class='bt_link' title='浙江省属企业上海金融人才专场招聘会在上海成功举行' target="_blank">浙江省属企业上海金融人才专场招聘会在上海成功举行</a>  <span class='bt_time' style="float:right;">2017-12-05</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/12/5/art_1389524_14233039.html' class='bt_link' title='我省第16次大规模组团赴上海招聘人才 230家单位推出岗位5800余个' target="_blank">我省第16次大规模组团赴上海招聘人才 230家单位推出岗位5800余个</a>  <span class='bt_time' style="float:right;">2017-12-05</span><br></li>]]></record>
<record><![CDATA[
<li style="height:50px;line-height:50px;border-bottom:1px dashed #e9e9e9"><span style="padding-right:8px"><img src='/picture/0/1711021544279186875.png' align='absmiddle' border='0'></span><a style='font:17px;line-height: 22px;color:#333333'  href='/art/2017/11/27/art_1389524_13861598.html' class='bt_link' title='首届浙江家庭服务业发展论坛在杭州成功举办' target="_blank">首届浙江家庭服务业发展论坛在杭州成功举办</a>  <span class='bt_time' style="float:right;">2017-11-27</span><br></li>]]></record>
</recordset>
</datastore></script></div>"""

import re
for match in re.finditer(r"<a style[\s\S]*?href='(?P<href>[\s\S]*?)'[\s\S]*?>(?P<title>[\s\S]*?)</a>[\s\S]*?>(?P<date>[\s\S]*?)<", html):
	print match.group("title")
	print match.group("href")
	print match.group("date")

