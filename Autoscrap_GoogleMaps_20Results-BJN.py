{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 339,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'html_attributions': [], 'results': [{'business_status': 'OPERATIONAL', 'formatted_address': 'Desa Tulungrejo, RT.1/RW.1, Tulungrejo, Trucuk, Kabupaten Bojonegoro, Jawa Timur 62155, Indonesia', 'geometry': {'location': {'lat': -7.157805799999999, 'lng': 111.8683847}, 'viewport': {'northeast': {'lat': -7.156441770107278, 'lng': 111.8696911798927}, 'southwest': {'lat': -7.159141429892722, 'lng': 111.8669915201073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 'name': 'Warung Makan Bu Sri', 'opening_hours': {'open_now': False}, 'photos': [{'height': 3024, 'html_attributions': ['<a href=\"https://maps.google.com/maps/contrib/112948296840851891841\">Nugroho Eko Widiyanto</a>'], 'photo_reference': 'ATtYBwKVLfFZfavrDV_Bn57p5qJp6CS4n4Oyr1vZ88r61bfbtVYWb4Vra9-7xChU0TzD3j0QPtDwLVwZ6ul28Gr1-k5wKy_NIBGbXCJjEqrC7to_ig1h-A-E6puLaqZAITmP1Z3kG93b9XdPX_23G7y2s30pXegFph_E_sScVxslpY0LdBph', 'width': 4032}], 'place_id': 'ChIJ0cijXrGBdy4RKuV52fwLyrA', 'plus_code': {'compound_code': 'RVR9+V9 Tulungrejo, Bojonegoro Regency, East Java', 'global_code': '6P4HRVR9+V9'}, 'rating': 4.4, 'reference': 'ChIJ0cijXrGBdy4RKuV52fwLyrA', 'types': ['restaurant', 'food', 'point_of_interest', 'establishment'], 'user_ratings_total': 138}, {'formatted_address': 'Trucuk, Bojonegoro Regency, East Java, Indonesia', 'geometry': {'location': {'lat': -7.1079966, 'lng': 111.8032005}, 'viewport': {'northeast': {'lat': -7.08433, 'lng': 111.8990401}, 'southwest': {'lat': -7.1651601, 'lng': 111.7814701}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/geocode-71.png', 'name': 'Trucuk', 'photos': [{'height': 1920, 'html_attributions': ['<a href=\"https://maps.google.com/maps/contrib/110368068898097754111\">A Google User</a>'], 'photo_reference': 'ATtYBwL4huCy545XvT6mwvdiebVXHPUe-Zh-RR16cPI07plOlf6bFBiktY2Lx1sSBOwUL_acYRlhZ7yNw9dTsW5O1X1zJVQLix5hVL_lADD3GpJHZoY90X34Nob84q5j3jS1pd3AtMF2LsyXE2AZkmgO_h4EBG6pXvSo6meNqxy5thHrYaAz', 'width': 2560}], 'place_id': 'ChIJWXtjbJF4dy4RhjJbf5hOkz4', 'reference': 'ChIJWXtjbJF4dy4RhjJbf5hOkz4', 'types': ['administrative_area_level_3', 'political']}, {'business_status': 'OPERATIONAL', 'formatted_address': 'Jl. Sawunggaling No.62, Ngrowo, Kabupaten, Kec. Bojonegoro, Kabupaten Bojonegoro, Jawa Timur 62111, Indonesia', 'geometry': {'location': {'lat': -7.1483036, 'lng': 111.8935991}, 'viewport': {'northeast': {'lat': -7.146936370107278, 'lng': 111.8948660298927}, 'southwest': {'lat': -7.149636029892722, 'lng': 111.8921663701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/civic_building-71.png', 'name': 'BPS Kabupaten Bojonegoro', 'opening_hours': {'open_now': True}, 'photos': [{'height': 720, 'html_attributions': ['<a href=\"https://maps.google.com/maps/contrib/100981239632498458254\">Dean Adit Prapanca</a>'], 'photo_reference': 'ATtYBwLg9rmR3AHT_Sc9lPPH9MDcQxZ1nkH9snotA3fH-P-YO-o_jWwO2N4vrbfHbXya1m4_qdvLV0H-oA6J4IR9GBiWCaGisfZUnddoI8CWk1orYkrEr8jTGaxW5PlOPLFB6Mod1CZS80ZNyPkbEFPjpzmP5-j4PEASRTIrFUqQ8Yh7wh1R', 'width': 1280}], 'place_id': 'ChIJ081oNiCHdy4R_I7XD-8DKVI', 'plus_code': {'compound_code': 'VV2V+MC Ngrowo, Bojonegoro Regency, East Java', 'global_code': '6P4HVV2V+MC'}, 'rating': 3.8, 'reference': 'ChIJ081oNiCHdy4R_I7XD-8DKVI', 'types': ['point_of_interest', 'establishment'], 'user_ratings_total': 5}], 'status': 'OK'}\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import csv\n",
    "import requests\n",
    "import time\n",
    "\n",
    "url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Warkop+in+Tulungrejo+Kecamatan Trucuk+Bojonegoro&key=AIzaSyCilGLcfaIJpwMcXje_Oyp8wWB9MNTr32Q'\n",
    "\n",
    "headers={'content-type':'application/json',\n",
    "         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0'}\n",
    "\n",
    "def csv_write():\n",
    "    csvfile =open('google_maps_Tulungrejo_Trucuk.csv','w') \n",
    "    writer = csv.writer(csvfile, delimiter=',')\n",
    "    writer.writerow([\"name\",\"lat\",\"long\",\"vicinity\"])\n",
    "\n",
    "    response = requests.get(url=url, headers=headers).json()\n",
    "    for obj in response['results']:\n",
    "        writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng'],obj['formatted_address']])\n",
    "        \n",
    "    \n",
    "    else:\n",
    "        print(response)\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    csv_write()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
