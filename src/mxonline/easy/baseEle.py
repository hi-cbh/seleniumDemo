

class BaseEle(object):


    url_login = "http://120.79.201.246:8088/login/"
    url_index = "http://120.79.201.246:8088/"
    url_xadmin = "http://120.79.201.246:8088/xadmin/"

    input_username="id=>account_l"

    input_password="id=>password_l"

    btn_login="id=>jsLoginBtn"

    swipe_windows="window.scrollTo(100,250);"

    link_courses="link_text=>公开课"

    link_teachers="link_text=>授课教师"

    link_orgs="link_text=>授课机构"

    # 课程列表（主题）
    list_course = "//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2"

    course_detail_fav="id=>jsLeftBtn"

    course_detail_study="xpath=>//div[@class='buy btn']"

    course_detail_org_fav="id=>jsRightBtn"

    # 教师模块
    list_teacher = "//*[@class='left']//dl[@class='des']//dd[*]/a/h1"

    teacher_detail_fav="id=>jsLeftBtn"

    teacher_detail_org_fav="id=>jsRightBtn"

    list_orgs="//*[@class='left']//dl[@class='des difdes']//div[*]/a/h1"

    org_detail_fav = "xpath=>//div[contains(@class,'collectionbtn')]"
    # org_detail_fav = "link_text=>收藏"

    # 组织模块




    xadmin_username="id=>id_username"

    xadmin_password="id=>id_password"

    xadmin_btn = "xpath=>//*[@class='btn btn-lg btn-primary btn-block']"



BaseEle = BaseEle()


