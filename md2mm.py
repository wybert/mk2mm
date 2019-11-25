
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET
import markdown
 
def get_tag_list(markdown_str):

#   解析 markdown为html
    # markdown = mistune.Markdown()
    # html = markdown(markdown_str)

    # 使用pytrhon markdown
    html = markdown.markdown(markdown_str)

#   使用beautiful soup解析 html
    soup = BeautifulSoup(html, "lxml")

#   找到所有的标题
    heads = soup.find_all(["h1", "h2", "h3", "h4", "h5"])

#   带解析的标题列表
    tag_list = []
    for item in heads:
        temp = {}
        temp["tag_name"] = item.name
        temp["text"] = item.text
        tag_list.append(temp)

    return tag_list


def get_km_node_list(t_list):

#  根据 tag list 创建km的node的list
    node_list = []
    for item in t_list:
        temp = {}
        node = {"data": {"text": item["text"]}, "children": []}
        temp["node"] = node
        temp["tag_name"] = item["tag_name"]
        node_list.append(temp)

    return node_list

def read_markdown(file_name):
    
    with open(file_name,"r",encoding = "utf-8") as fl:
        markdown_str = fl.read()
    return markdown_str

def save_km(km_dict,file_name):

    data = json.dumps(km_dict)
    with open(file_name,"w") as fl:
        fl.write(data)


def to_km(node_list):

#  根据node list的先后顺序，按照步骤和标签创建 km的脑图数据结构

    template = {"root": {}, "template": "right",
            "theme": "fresh-blue", "version": "1.4.43"}

    for node in node_list:
        if node["tag_name"] == "h1":
            template["root"] = node["node"]
        
        if node["tag_name"] == "h2":
            template["root"]["children"].append(node["node"])

        if node["tag_name"] == "h3":
            template["root"]["children"][-1]["children"].append(node["node"])

        if node["tag_name"] == "h4":
            template["root"]["children"][-1]["children"][-1]["children"].append(node["node"])

        if node["tag_name"] == "h5":
            template["root"]["children"][-1]["children"][-1]["children"][-1]["children"].append(
                node["node"])
    
    return template

def to_mm(tag_list):

    map_doc = ET.Element('map',{"version":"freeplane 1.6.0"})
    for node in tag_list:
        if node["tag_name"] == "h1":
            h1 = ET.SubElement(map_doc,"node",{"TEXT":node["text"]}) 
        if node["tag_name"] == "h2":
            h2 = ET.Element("node",{"TEXT":node["text"]})
            h1.append(h2)
        if node["tag_name"] == "h3":
            h3 = ET.Element("node",{"TEXT":node["text"]})
            h2.append(h3)
        if node["tag_name"] == "h4":
            h4 = ET.Element("node",{"TEXT":node["text"]})
            h3.append(h4)
        if node["tag_name"] == "h5":
            h5 = ET.Element("node",{"TEXT":node["text"]})
            h4.append(h5)
    tree = ET.ElementTree(map_doc) 
    return tree

def mk2km(input_fileName,output_fileName):

    markdown_str = read_markdown(input_fileName)

    ## 保存km
    tag_list = get_tag_list(markdown_str)
    node_list = get_km_node_list(tag_list)
    template = to_km(node_list)
    save_km(template, output_fileName)


def mk2mm(input_fileName, output_fileName):

    markdown_str = read_markdown(input_fileName)
    ## 保存km
    tag_list = get_tag_list(markdown_str)
    tree = to_mm(tag_list)
## 保存mm
    tree.write(output_fileName)

# test

if __name__ == '__main__':

    mk2km("test.md", "test.km")
    mk2mm("test.md", "test.mm")

    # markdown_str = read_markdown("out_v2.7.md")
    # tag_list = get_tag_list(markdown_str)
    # print(tag_list)