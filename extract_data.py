import re
from bs4 import BeautifulSoup

def extract_data_sequence_and_h1(html_file_path):
    """
    从HTML文件中提取每个<article>标签中的data-sequence属性值和对应的<h1>标签内容
    
    参数:
        html_file_path (str): HTML文件路径
        
    返回:
        list: 包含(data-sequence, h1内容)元组的列表
    """
    # 读取HTML文件
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 查找所有<article class="card">标签
    articles = soup.find_all('article', class_='card')
    
    results = []
    
    for article in articles:
        # 获取data-sequence属性值
        data_sequence = article.get('data-sequence')
        
        if data_sequence:
            # 查找<article>下的<div>下的<h1>标签
            div = article.find('div', class_='pd-6 overflow-hidden bg-card container radius-1')
            if div:
                h1 = div.find('h1')
                if h1:
                    h1_content = h1.get_text(strip=True)
                    results.append((data_sequence, h1_content))
    
    return results

if __name__ == "__main__":
    # 指定HTML文件路径
    html_file_path = "/Users/tangwan/TraeProjects/test/jetbrains.html"
    
    # 提取数据
    extracted_data = extract_data_sequence_and_h1(html_file_path)
    
    # 打印结果
    for data_sequence, h1_content in extracted_data:
        print(f"{data_sequence} = {h1_content}")