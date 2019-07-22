import os
import xml.dom.minidom
def xml_to_text(input_filename,output_path):
    """
    :param input_filename: 从NCBI上下载的xml文件
    :return:  每一篇文章的内容
    """
    mydom = xml.dom.minidom.parse(input_filename)
    #root = mydom.documentElement
    article_set = mydom.getElementsByTagName('article')  # 获取XML节点对象列表,xUsers 为一个列表，包含一个元素，即为根节点

    for i in article_set:
        # 提取PMC-ID
        pmc_id = '' # 类型为str
        article_id = i.getElementsByTagName('article-id')
        for id in article_id:
            if(id.getAttribute("pub-id-type") == "pmc"):
                pmc_id = id.childNodes[0].data
        print(pmc_id)

        with open( output_path +"PMC_%s.txt" % (pmc_id), "a", encoding="utf-8") as output_file:
            # 提取title
            article_titles = i.getElementsByTagName('article-title')
            if(len(article_titles)):
                article_title = article_titles[0]
                title = ""
                try:
                    for t in article_title.childNodes:
                        if (t.nodeName == "#text"):
                            title += t.nodeValue.replace('\n', ' ').replace('\n', ' ')
                        else:
                            title += t.childNodes[0].data
                except(Exception):
                    continue
                title.replace('\n', ' ').replace("\n", ' ')
                output_file.write(title + "\n")

            #提取abstract
            article_front = i.getElementsByTagName('article-meta')
            for ab in article_front:
                abstract_p = ab.getElementsByTagName("p")
                try:
                    for a in abstract_p:
                        abstr = ""
                        if a.parentNode.nodeName == "abstract":
                            for w in a.childNodes:
                                if (w.nodeName == "#text"):
                                    abstr += w.nodeValue.replace('\n', ' ').replace('\n', ' ')
                                else:
                                    abstr += w.childNodes[0].data
                        output_file.write(abstr+"\n")
                except(Exception):
                    continue


             # 提取段落
            article_body = i.getElementsByTagName('body')
            for j in article_body:  # j为一个body 结点(类型为Element）
                paragraphs = j.getElementsByTagName('p')
                try:
                    for k in paragraphs:    # k为每一个
                        para = ""
                        if (k.parentNode.nodeName == "sec" or k.parentNode.nodeName == "body"
                                or k.parentNode.nodeName == "list-item" or k.parentNode.nodeName == "boxed-text"
                                or k.parentNode.nodeName == "disp-quote"):
                            for c in k.childNodes:
                                if (c.nodeName == "#text"):
                                    para += c.nodeValue.replace('\n', ' ').replace('\n', ' ')
                                if (c.nodeName == "italic"):
                                    para += c.childNodes[0].data
                                else:
                                    continue
                            output_file.write(para + "\n")
                        else:
                            continue

                except(Exception):
                    continue

if __name__ == "__main__":

    xml_file_path = "/media/EXTend2018/Fuyibao2018/NCBI/Fulltext2017/"
    output_path = "/media/EXTend2018/Fuyibao2018/Process_NCBI_article/2017Fulltext/"

    file_list = os.listdir(xml_file_path)
    for file in file_list:
        print(file)
        xml_to_text(xml_file_path + file, output_path)
    print("done")
