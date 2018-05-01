from urllib.request import Request, urlopen
import urllib
import re
import csv
import urllib.parse
import urllib.request
import time
feature_phone_data =[]

def clean(x, loc=2):
    return str(x)[loc:][:-loc]

print("flipkart print");
for line in open("data1.txt", encoding='utf-8'):
    req = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
    abc = urlopen(req).read()
    """pspecs = ''
    pimages = ''
    # Catagory Tree
    match_category = re.findall(r'(?is)<li class="fk-inline-block">.*?<strong>', str(abc));
    catagory =re.sub(r'(?is)</a>', r'->', str(match_category))
    product_catagory = re.sub(r'(?is)<.*?>|\\t|\\n|\\|&nbsp;&gt;&nbsp;',r' ',str(catagory));
    product_catagory = clean(re.sub(r'(?is)\s{2,}',r' ',str(product_catagory)));"""

    # Product Name
    match_title = re.findall(r'(?is)<h1 class="title" itemprop="name">.*?</div>', str(abc));
    product_name = clean(re.sub(r'(?is)<h1 class="title" itemprop="name">(.*?)</div>',r'\1',str(match_title)));
    product1 = re.sub(r'(?is)<.*?>|\\t|\\n|\\',r'',str(product_name));
    product_title = (re.sub(r'(?is)\s{2,}',r' ',str(product1)));

    # Product Retail Price
    match_rprice = re.findall(r'(?is)List Price|MRP\s*:.*?<span class="price">.*?</span>.*?<span', str(abc));
    product_rprice = clean(re.sub(r'(?is)List Price\s*:|MRP\s*:.*?<span class="price">(.*?)</span>.*?<span',r'\1',str(match_rprice)));

    # Product Offer Price
    match_ofprice = re.findall(r'(?is)<span class="selling-price.*?data-eVar48.*?>.*?</span>', str(abc));
    product_ofprice = clean(re.sub(r'(?is)<span class="selling-price.*?>(.*?)</span>',r'\1',str(match_ofprice)));
    print (product_ofprice)

    # Details
    match_details = re.findall(r'(?is)<ul class="key-specifications.*?>.*?</div', str(abc));
    match_detail =re.sub(r'(?is)</li>|</div', r' , ', str(match_details))
    product_detail = re.sub(r'(?is)<.*?>|\\n|\\',r'',str(match_detail));
    product_details = clean(re.sub(r'(?is)\s{2,}',r'',str(product_detail)));

    # Details
    match_details1 = re.findall(r'(?is)<ul class="keyFeaturesList">.*?</div', str(abc));
    match_detail1 =re.sub(r'(?is)</li>|</div', r' , ', str(match_details1))
    product_detail1 = re.sub(r'(?is)<.*?>|\\n|\\',r'',str(match_detail1));
    product_details1 = clean(re.sub(r'(?is)\s{2,}',r'',str(product_detail1)));

    # description   
    match_descrip = re.findall(r'(?is)<div class="description-text">.*?</div', str(abc));
    product_description = clean(re.sub(r'(?is)<div class="description-text">(.*?)</div',r'\1',str(match_descrip)));

    # Other Convenience Features   
    match_Convenience_Features = re.findall(r'(?is)class="specsKey">Other Convenience Features</td>.*?>.*?<', str(abc));
    prod_Convenience_Features =re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'', str(match_Convenience_Features))
    product_Convenience_Features = clean(re.sub(r'(?is)class="specsKey">Other Convenience Features</td>.*?>(.*?)<',r'',str(prod_Convenience_Features)));

    # Brand
    match_brand = re.findall(r'(?is)class="specsKey">Brand</td>.*?>.*?<', str(abc));
    product_branding = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_brand));
    product_brand = clean(re.sub(r'(?is)class="specsKey">Brand</td>.*?>(.*?)<',r'\1',str(product_branding)));

    # Model Name
    match_model= re.findall(r'(?is)class="specsKey">Model Name</td>.*?>.*?<', str(abc));
    product_model = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_model));
    product_model = clean(re.sub(r'(?is)class="specsKey">Model Name</td>.*?>(.*?)<',r'\1',str(product_model)));

    # Model ID
    match_model_id= re.findall(r'(?is)class="specsKey">Model ID</td>.*?>.*?<', str(abc));
    product_model_id = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_model_id));
    product_model_id = clean(re.sub(r'(?is)class="specsKey">Model ID</td>.*?>(.*?)<',r'\1',str(product_model_id)));

    # Handset Color
    match_color = re.findall(r'(?is)class="specsKey">Handset Color</td>.*?>.*?<', str(abc));
    prod_match_color = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_color));
    product_match_color = clean(re.sub(r'(?is)class="specsKey">Handset Color</td>.*?>(.*?)<',r'\1',str(prod_match_color)));
    #print(product_capacity)

    # Keypad
    match_Keypad = re.findall(r'(?is)class="specsKey">Keypad</td>.*?>.*?<', str(abc));
    prod_match_Keypad = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Keypad));
    product_match_Keypad = clean(re.sub(r'(?is)class="specsKey">Keypad</td>.*?>(.*?)<',r'\1',str(prod_match_Keypad)));

    # SIM Size
    match_SIM_Size = re.findall(r'(?is)class="specsKey">SIM Size</td>.*?>.*?<', str(abc));
    prod_match_SIM_Size = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_SIM_Size));
    prod_SIM_Size = clean(re.sub(r'(?is)class="specsKey">SIM Size</td>.*?>(.*?)<',r'\1',str(prod_match_SIM_Size)));

    # Call Features
    match_call_feat = re.findall(r'(?is)class="specsKey">Call Features</td>.*?>.*?<', str(abc));
    prod_call_feat = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_call_feat));
    product_call_feat = clean(re.sub(r'(?is)class="specsKey">Call Features</td>.*?>(.*?)<',r'\1',str(prod_call_feat)));
    
    # Touch Screen
    match_touch_screen = re.findall(r'(?is)class="specsKey">Touch Screen</td>.*?>.*?<', str(abc));
    prod_touch_screen = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_touch_screen));
    product_touch_screen = clean(re.sub(r'(?is)class="specsKey">Touch Screen</td>.*?>(.*?)<',r'\1',str(prod_touch_screen)));

    # SIM Type
    match_sim_type = re.findall(r'(?is)class="specsKey">SIM Type</td>.*?>.*?<', str(abc));
    prod_sim_type = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_sim_type));
    product_sim_type = clean(re.sub(r'(?is)class="specsKey">SIM Type</td>.*?>(.*?)<',r'\1',str(prod_sim_type)));

    # Rear Camera
    match_rear_camera = re.findall(r'(?is)class="specsKey">Rear Camera</td>.*?>.*?<', str(abc));
    prod_rear_camera = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_rear_camera));
    product_rear_camera = clean(re.sub(r'(?is)class="specsKey">Rear Camera</td>.*?>(.*?)<',r'\1',str(prod_rear_camera)));

    # Front Facing Camera
    match_front_camera = re.findall(r'(?is)class="specsKey">Front Facing Camera</td>.*?>.*?<', str(abc));
    prod_front_camera = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_front_camera));
    product_front_camera = clean(re.sub(r'(?is)class="specsKey">Front Facing Camera</td>.*?>(.*?)<',r'\1',str(prod_front_camera)));

    # Audio Jack
    match_audio_jack= re.findall(r'(?is)class="specsKey">Audio Jack</td>.*?>.*?<', str(abc));
    prod_audio_jack = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_audio_jack));
    product_audio_jack = clean(re.sub(r'(?is)class="specsKey">Audio Jack</td>.*?>(.*?)<',r'\1',str(prod_audio_jack)));

    # HDMI Port
    match_hdmi_port= re.findall(r'(?is)class="specsKey">HDMI Port</td>.*?>.*?<', str(abc));
    prod_hdmi_port = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_hdmi_port));
    product_hdmi_port = clean(re.sub(r'(?is)class="specsKey">HDMI Port</td>.*?>(.*?)<',r'\1',str(prod_hdmi_port)));

    # Wifi
    match_Wifi= re.findall(r'(?is)>INTERNET & CONNECTIVITY.*?class="specsKey">Wifi</td>.*?>.*?<', str(abc));
    prod_Wifi = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Wifi));
    product_Wifi = clean(re.sub(r'(?is)>INTERNET & CONNECTIVITY.*?class="specsKey">Wifi</td>.*?>(.*?)<',r'\1',str(prod_Wifi)));

    # USB Connectivity
    match_usb= re.findall(r'(?is)class="specsKey">USB Connectivity</td>.*?>.*?<', str(abc));
    prod_usb = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_usb));
    product_usb = clean(re.sub(r'(?is)class="specsKey">USB Connectivity</td>.*?>(.*?)<',r'\1',str(prod_usb)));

    # Supported Languages
    match_lang= re.findall(r'(?is)class="specsKey">Supported Languages</td>.*?>.*?<', str(abc));
    prod_lang = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_lang));
    product_lang = clean(re.sub(r'(?is)class="specsKey">Supported Languages</td>.*?>(.*?)<',r'\1',str(prod_lang)));

    # Additional Features
    match_add_feat= re.findall(r'(?is)class="specsKey">Additional Features</td>.*?>.*?<', str(abc));
    prod_add_feat = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_add_feat));
    product_add_feat = clean(re.sub(r'(?is)class="specsKey">Additional Features</td>.*?>(.*?)<',r'\1',str(prod_add_feat)));
    
    # warranty summary
    match_warranty = re.findall(r'(?is)class="specsKey">Warranty Summary</td>.*?>.*?<', str(abc));
    product_warranties = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_warranty));
    product_warranty = clean(re.sub(r'(?is)class="specsKey">Warranty Summary</td>.*?>(.*?)<',r'\1',str(product_warranties)));

    # Covered in Warranty
    match_cov_warranty = re.findall(r'(?is)class="specsKey">Covered in Warranty</td>.*?>.*?<', str(abc));
    product_cov_warranty = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_cov_warranty));
    product_cov_warranty = clean(re.sub(r'(?is)class="specsKey">Covered in Warranty</td>.*?>(.*?)<',r'\1',str(product_cov_warranty)));

    # Warranty Service Type
    match_service_warranty = re.findall(r'(?is)class="specsKey">Warranty Service Type</td>.*?>.*?<', str(abc));
    product_service_warranty = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_service_warranty));
    product_service_warranty = clean(re.sub(r'(?is)class="specsKey">Warranty Service Type</td>.*?>(.*?)<',r'\1',str(product_service_warranty)));

    # Not Covered in Warranty
    match_not_cov_warranty = re.findall(r'(?is)class="specsKey">Not Covered in Warranty</td>.*?>.*?<', str(abc));
    product_not_cov_warranty = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_not_cov_warranty));
    product_not_cov_warranty = clean(re.sub(r'(?is)class="specsKey">Not Covered in Warranty</td>.*?>(.*?)<',r'\1',str(product_not_cov_warranty)));

    # Display Size
    match_dp_size = re.findall(r'(?is)Display.*?class="specsKey">Size</td>.*?>.*?<', str(abc));
    product_dp_size = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_dp_size));
    product_dp_size = clean(re.sub(r'(?is)Display.*?class="specsKey">Size</td>.*?>(.*?)<',r'\1',str(product_dp_size)));

    # Resolution
    match_Resolution = re.findall(r'(?is)Display.*?class="specsKey">Resolution</td>.*?>.*?<', str(abc));
    product_Resolution = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Resolution));
    product_Resolution = clean(re.sub(r'(?is)Display.*?class="specsKey">Resolution</td>.*?>(.*?)<',r'\1',str(product_Resolution)));

    # Display Type
    match_dp_type = re.findall(r'(?is)Display.*?class="specsKey">Type</td>.*?>.*?<', str(abc));
    product_dp_type = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_dp_type));
    product_dp_type = clean(re.sub(r'(?is)Display.*?class="specsKey">Type</td>.*?>(.*?)<',r'\1',str(product_dp_type)));

    # Form
    match_Form = re.findall(r'(?is)Display.*?class="specsKey">Form</td>.*?>.*?<', str(abc));
    product_Form = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Form));
    product_Form = clean(re.sub(r'(?is)Display.*?class="specsKey">Form</td>.*?>(.*?)<',r'\1',str(product_Form)));

    # Zoom
    match_zoom = re.findall(r'(?is)Camera.*?class="specsKey">Zoom</td>.*?>.*?<', str(abc));
    product_zoom = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_zoom));
    product_zoom = clean(re.sub(r'(?is)Camera.*?class="specsKey">Zoom</td>.*?>(.*?)<',r'\1',str(product_zoom)));

    # Flash
    match_Flash= re.findall(r'(?is)class="specsKey">Flash</td>.*?>.*?<', str(abc));
    prod_Flash = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Flash));
    product_Flash = clean(re.sub(r'(?is)class="specsKey">Flash</td>.*?>(.*?)<',r'\1',str(prod_Flash)));

    # Video Recording
    match_video_recording= re.findall(r'(?is)class="specsKey">Video Recording</td>.*?>.*?<', str(abc));
    prod_video_recording = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_video_recording));
    product_video_recording = clean(re.sub(r'(?is)class="specsKey">Video Recording</td>.*?>(.*?)<',r'\1',str(prod_video_recording)));

    # Other Camera Features
    match_oth_cam_feat= re.findall(r'(?is)class="specsKey">Other Camera Features</td>.*?>.*?<', str(abc));
    prod_oth_cam_feat = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_oth_cam_feat));
    product_oth_cam_feat = clean(re.sub(r'(?is)class="specsKey">Other Camera Features</td>.*?>(.*?)<',r'\1',str(prod_oth_cam_feat)));

    # FM
    match_fm= re.findall(r'(?is)class="specsKey">FM</td>.*?>.*?<', str(abc));
    prod_fm = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_fm));
    product_fm = clean(re.sub(r'(?is)class="specsKey">FM</td>.*?>(.*?)<',r'\1',str(prod_fm)));

    # Video Player
    match_video_player= re.findall(r'(?is)class="specsKey">Video Player</td>.*?>.*?<', str(abc));
    prod_video_player = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_video_player));
    product_video_player = clean(re.sub(r'(?is)class="specsKey">Video Player</td>.*?>(.*?)<',r'\1',str(prod_video_player)));

    # Music Player
    match_music_player= re.findall(r'(?is)class="specsKey">Video Player</td>.*?>.*?<', str(abc));
    prod_music_player = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_music_player));
    product_music_player = clean(re.sub(r'(?is)class="specsKey">Video Player</td>.*?>(.*?)<',r'\1',str(prod_music_player)));

    # Sound Enhancement
    match_sound= re.findall(r'(?is)class="specsKey">Sound Enhancement</td>.*?>.*?<', str(abc));
    prod_sound = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_sound));
    product_sound = clean(re.sub(r'(?is)class="specsKey">Sound Enhancement</td>.*?>(.*?)<',r'\1',str(prod_sound)));

    # Ringtone
    match_Ringtone= re.findall(r'(?is)>Multimedia.*?class="specsKey">Ringtone</td>.*?>.*?<', str(abc));
    prod_Ringtone = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Ringtone));
    product_Ringtone = clean(re.sub(r'(?is)>Multimedia.*?class="specsKey">Ringtone</td>.*?>(.*?)<',r'\1',str(prod_Ringtone)));

    # display Color
    match_Color= re.findall(r'(?is)Display.*?class="specsKey">Color</td>.*?>.*?<', str(abc));
    prod_Color = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_Color));
    product_Color = clean(re.sub(r'(?is)Display.*?class="specsKey">Color</td>.*?>(.*?)<',r'\1',str(prod_Color)));

    # Phone Book Memory
    match_phone_book= re.findall(r'(?is)class="specsKey">Phone Book Memory</td>.*?>.*?<', str(abc));
    prod_phone_book = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_phone_book));
    product_phone_book = clean(re.sub(r'(?is)class="specsKey">Phone Book Memory</td>.*?>(.*?)<',r'\1',str(prod_phone_book)));

    # Call Memory
    match_call_mem= re.findall(r'(?is)class="specsKey">Call Memory</td>.*?>.*?<', str(abc));
    prod_call_mem = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_call_mem));
    product_call_mem = clean(re.sub(r'(?is)class="specsKey">Call Memory</td>.*?>(.*?)<',r'\1',str(prod_call_mem)));

    # SMS Memory
    match_sms_mem= re.findall(r'(?is)class="specsKey">SMS Memory</td>.*?>.*?<', str(abc));
    prod_sms_mem = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_sms_mem));
    product_sms_mem = clean(re.sub(r'(?is)class="specsKey">SMS Memory</td>.*?>(.*?)<',r'\1',str(prod_sms_mem)));

    # Important Apps
    match_imp_apps= re.findall(r'(?is)class="specsKey">Important Apps</td>.*?>.*?<', str(abc));
    prod_imp_apps = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_imp_apps));
    product_imp_apps = clean(re.sub(r'(?is)class="specsKey">Important Apps</td>.*?>(.*?)<',r'\1',str(prod_imp_apps)));

    # Talk Time
    match_talk_time= re.findall(r'(?is)class="specsKey">Talk Time</td>.*?>.*?<', str(abc));
    prod_talk_time = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_talk_time));
    product_talk_time = clean(re.sub(r'(?is)class="specsKey">Talk Time</td>.*?>(.*?)<',r'\1',str(prod_talk_time)));

    # Standby Time
    match_stand_time= re.findall(r'(?is)class="specsKey">Standby Time</td>.*?>.*?<', str(abc));
    prod_stand_time = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_stand_time));
    product_stand_time = clean(re.sub(r'(?is)class="specsKey">Standby Time</td>.*?>(.*?)<',r'\1',str(prod_stand_time)));

    # Battery Type
    match_batt_type= re.findall(r'(?is)Battery.*?class="specsKey">Type</td>.*?>.*?<', str(abc));
    prod_batt_type = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_batt_type));
    product_batt_type = clean(re.sub(r'(?is)Battery.*?class="specsKey">Type</td>.*?>(.*?)<',r'\1',str(prod_batt_type)));

    # Expandable Memory
    match_expan_mem= re.findall(r'(?is)class="specsKey">Expandable Memory</td>.*?>.*?<', str(abc));
    prod_expan_mem = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_expan_mem));
    product_expan_mem = clean(re.sub(r'(?is)class="specsKey">Expandable Memory</td>.*?>(.*?)<',r'\1',str(prod_expan_mem)));

    # Operating Freq
    match_oper_freq= re.findall(r'(?is)class="specsKey">Operating Freq</td>.*?>.*?<', str(abc));
    prod_oper_freq = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_oper_freq));
    product_oper_freq = clean(re.sub(r'(?is)class="specsKey">Operating Freq</td>.*?>(.*?)<',r'\1',str(prod_oper_freq)));

    # OS
    match_os= re.findall(r'(?is)Platform.*?class="specsKey">OS</td>.*?>.*?<', str(abc));
    prod_os = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_os));
    product_os = clean(re.sub(r'(?is)Platform.*?class="specsKey">OS</td>.*?>(.*?)<',r'\1',str(prod_os)));

    
    # image urls
    match_image = re.findall(r'(?is)class="imgWrapper">.*?data-src=".*?".*?</div', str(abc));
    product_img = re.sub(r'(?is)\s{2,}|\\t|\\n|\\',r'',str(match_image));
    product_images = clean(re.sub(r'(?is)class="imgWrapper">.*?data-src="(.*?)".*?</div',r'\1',str(product_img)));
    #print(product_images)

    feature_phone = {'Title' : product_title,
                 'Retail Price' : product_rprice,
                 'Offer Price' : product_ofprice,
                 'Details' : product_details,
                 'Details1' : product_details1,
                 'Description':product_description,
                 'Description1':product_Convenience_Features,
                 'Brand':product_brand,   
                 'Model Name':product_model,
                 'Model ID':product_model_id,
                 'Handset Color':product_match_color,
                 'Keypad':product_match_Keypad,
                 'SIM Size':prod_SIM_Size,
                 'Call Features':product_call_feat,
                 'Touch Screen':product_touch_screen,
                 'SIM Type':product_sim_type,
                 'Rear Camera':product_rear_camera,
                 'Front Facing Camera':product_front_camera,
                 'Audio Jack':product_audio_jack,
                 'HDMI Port':product_hdmi_port,
                 'Wifi':product_Wifi,
                 'USB Connectivity':product_usb,
                 'Supported Languages':product_lang,
                 'Additional Features':product_add_feat,
                 'warranty summary':product_warranty,
                 'Covered in Warranty':product_cov_warranty,
                 'Warranty Service Type':product_service_warranty,
                 'Not Covered in Warranty':product_not_cov_warranty,
                 'Display Size':product_dp_size,
                 'Resolution':product_Resolution,
                 'Display Type':product_dp_type,
                 'Form':product_Form,
                 'Zoom':product_zoom,
                 'Flash':product_Flash,
                 'Video Recording':product_video_recording,
                 'Other Camera Features':product_oth_cam_feat,
                 'FM':product_fm,
                 'Video Player':product_video_player,
                 'Music Player':product_music_player,
                 'Sound Enhancement':product_sound,
                 'Ringtone':product_Ringtone,
                 'display Color':product_Color,
                 'Phone Book Memory':product_phone_book,
                 'Call Memory':product_call_mem,
                 'SMS Memory':product_sms_mem,
                 'Important Apps':product_imp_apps,
                 'Talk Time':product_talk_time,
                 'Standby Time':product_stand_time,
                 'Battery Type':product_batt_type,
                 'Expandable Memory':product_expan_mem,
                 'Operating Freq':product_oper_freq,
                 'Operating System':product_os,
                 'IMAGE':product_images
                 }
    
    feature_phone_data.append(feature_phone)
    with open('details_feature_phones.csv', 'w') as csvfile:
        fieldnames =['Title',
                 'Retail Price',
                 'Offer Price',
                 'Details',
                 'Details1',
                 'Description',
                 'Description1',
                 'Brand',   
                 'Model Name',
                 'Model ID',
                 'Handset Color',
                 'Keypad',
                 'SIM Size',
                 'Call Features',
                 'Touch Screen',
                 'SIM Type',
                 'Rear Camera',
                 'Front Facing Camera',
                 'Audio Jack',
                 'HDMI Port',
                 'Wifi',
                 'USB Connectivity',
                 'Supported Languages',
                 'Additional Features',
                 'warranty summary',
                 'Covered in Warranty',
                 'Warranty Service Type',
                 'Not Covered in Warranty',
                 'Display Size',
                 'Resolution',
                 'Display Type',
                 'Form',
                 'Zoom',
                 'Flash',
                 'Video Recording',
                 'Other Camera Features',
                 'FM',
                 'Video Player',
                 'Music Player',
                 'Sound Enhancement',
                 'Ringtone',
                 'display Color',
                 'Phone Book Memory',
                 'Call Memory',
                 'SMS Memory',
                 'Important Apps',
                 'Talk Time',
                 'Standby Time',
                 'Battery Type',
                 'Expandable Memory',
                 'Operating Freq',
                 'Operating System',
                 'IMAGE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entries in feature_phone_data:
            writer.writerow(entries)
    print(line)
    time.sleep(1)
