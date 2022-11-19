import cv2 
import numpy as np
 import time 
import pyzbar.pyzbar as pyzbar
 from pyzbar.pyzbar import decode
 from ibmcloudant.cloudant_v1 import CloudantV1
 from ibmcloudant import CouchDbSessionAuthenticator
  from ibm_cloud_sdk_core.authenticators imporBasicAuthenticator 
 
authenticator = BasicAuthenticator('apikey-v2-125rwcp4ifi6zz2ly1cq0kakyjn98du2ysgc72h53lzi', 
'af693938842290ec2c254461754447b5') service = CloudantV1(authenticator=authenticator) 
 
service.set_service_url('https://apikey-v2-
125rwcp4ifi6zz2ly1cq0kakyjn98du2ysgc72h53lzi:af693938842290ec2c254461754447b5@82d874994395-4f46-a190-6a186bee5051-bluemix.cloudantnosqldb.appdomain.cloud') 
 
cap= cv2.VideoCapture(0) font = cv2.FONT_HERSHEY_PLAIN while True: 
   _, frame = cap.read()    decodedObjects = pyzbar.decode(frame)    for obj in decodedObjects:       #print ("Data", obj.data)       a=obj.data.decode('UTF-8')       cv2.putText(frame, "Ticket", (50, 50), font, 2, 	(255, 0, 0), 3) 
      #print (a) 	 	 
      try: 
         response = service.get_document(db='booking',doc_id = a).get_result()          print(response)          time.sleep(5)       except Exception as e: 
         print("NOT A VALID TICKER")          time.sleep(5) 
          
   cv2.imshow("Frame",frame)    if cv2.waitKey(1) & 0xFF ==ord('q'): 
      break 
 	 	 
cap.release() cv2.destroyAllWindows() 
client.disconnect() 
 
