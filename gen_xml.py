import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def add_boxes(boxes,key,value):
	try:
		boxes[key].append(value)# xmin,ymin,xmax,ymax
	except KeyError:
		boxes[key] = [value]
	
def gen_boxes():
	boxes = {}
	add_boxes(boxes,'circle',[136,217,166,208])
	add_boxes(boxes,'circle',[163,220,190,210])
	return boxes

def gen_xml(jpg_name):
	root_name = ET.Element('annotation')
	file_name = ET.SubElement(root_name,'filename')
	file_name.text = jpg_name.split('.')[0]
	return root_name

def write_boxes(root,boxes):
	for key in boxes:
		ll = boxes[key]
		for _,value in enumerate(ll):
			print(key,value)
			node_name = ET.SubElement(root,'object')
			node1 = ET.SubElement(node_name,'name')
			node1.text = key
			node2 = ET.SubElement(node_name,'bndbox')
			node21 = ET.SubElement(node2,'xmin')
			node21.text = str(value[0])
			node22 = ET.SubElement(node2,'ymin')
			node22.text = str(value[1])
			node23 = ET.SubElement(node2,'xmax')
			node23.text = str(value[2])
			node24 = ET.SubElement(node2,'ymax')
			node24.text = str(value[3])
	return root

def write_xml(xml_name,root_name):
	rough_string = ET.tostring(root_name,'utf-8')
	reared_content = minidom.parseString(rough_string)
	with open(xml_name,'w+') as fs:
		reared_content.writexml(fs,addindent=' ',newl='\n',encoding='utf-8')
	return root_name
	
def main_test():
	root = gen_xml('001.jpg')
	boxes = gen_boxes()
	root = write_boxes(root,boxes)
	write_xml('001.xml',root)

if __name__ == '__main__':
	main_test()
