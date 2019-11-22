#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Script used to modified csv files"""

__author__ = "Tierbolg"
__copyright__ = "Tierbolg"
__credits__ = ["Gilberto", "Oma"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "tierbolg@outlook.com"
__status__ = "Development"

import csv
classArray=[]

class Rowformatted:
    Sales_Record_Number = ''
    User_Id = ''
    Buyer_Full_name = ''
    Buyer_Phone_Number = ''
    Buyer_Email = ''
    Buyer_Address_1 = ''
    Buyer_Address_2 = ''
    Buyer_TownCity = ''
    Buyer_County = ''
    Buyer_Postcode = ''
    Buyer_Country = ''
    Item_Number = ''
    Item_Title = ''
    Custom_Label = ''
    Quantity = ''
    Sale_Price = ''
    Included_VAT_Rate = ''
    Postage_and_Packaging = ''
    Insurance = ''
    Cash_on_delivery_fee = ''
    Total_Price = ''
    Payment_Method = ''
    Sale_Date = ''
    Checkout_Date = ''
    Paid_on_Date = ''
    Dispatch_Date_ = ''
    Invoice_date = ''
    Invoice_number = ''
    Feedback_left = ''
    Feedback_received = ''
    Notes_to_yourself = ''
    Unique_Product_Id = ''
    Private_Field = ''
    ProductIDType = ''
    ProductIDValue = ''
    ProductIDValue2 = ''
    PayPal_Transaction_ID = ''
    Delivery_Service = ''
    Cash_on_delivery_option = ''
    Transaction_ID = ''
    Order_ID = ''
    Variation_Details = ''
    Global_Shipping_Programme = ''
    Global_Shipping_Reference_ID = ''
    Click_and_Collect = ''
    Click_and_Collect_Reference = ''
    Post_To_Address_1 = ''
    Post_To_Address_2 = ''
    Post_To_City = ''
    Post_To_County = ''
    Post_To_Postcode = ''
    Post_To_Country = ''
    eBay_Plus = ''
    pass


def readcsv(fileToRead):
    
    with open(fileToRead, newline='') as filetoparse:
        reader = csv.reader(filetoparse, delimiter=',', quoting=csv.QUOTE_ALL)
        # Skip the header
        next(reader)        
        for row in reader:
            if(row[0] == '' and row[1] == '') or ('record' in row[0]):
                continue
            print(row)
            if 'record' in row[1]:
                rowTostore = Rowformatted()
                rowTostore.Sales_Record_Number = row[0]
                rowTostore.User_Id='record(s) downloaded'
                rowTostore.Buyer_Full_name='from'
                rowTostore.Buyer_Address_1='to'
                classArray.append(rowTostore)
                continue

            if 'Seller' in row[0]:
                rowTostore = Rowformatted()
                separatedValue=row[0].split(':')
                rowTostore.Sales_Record_Number = separatedValue[0]+':'+separatedValue[1]+'@gmail.com'
                classArray.append(rowTostore)
                continue


            rowTostore = Rowformatted()
            rowTostore.Sales_Record_Number = row[0]
            rowTostore.User_Id =row[44]
            rowTostore.Buyer_Full_name=row[3]
            rowTostore.Buyer_Phone_Number=row[13]
            rowTostore.Buyer_Email=row[4]
            rowTostore.Buyer_Address_1=row[6]
            rowTostore.Buyer_Address_2=row[7]
            rowTostore.Buyer_TownCity=row[8]
            rowTostore.Buyer_County=row[9]
            rowTostore.Buyer_Postcode=row[10]
            rowTostore.Buyer_Country=row[11]
            rowTostore.Item_Number=row[20]
            rowTostore.Item_Title=row[21]
            rowTostore.Custom_Label=row[22]
            rowTostore.Quantity=row[24]
            #rowTostore.Sale_Price
            rowTostore.Included_VAT_Rate=row[27]
            rowTostore.Postage_and_Packaging=row[26]
            #rowTostore.Insurance
            #rowTostore.Cash_on_delivery_fee
            rowTostore.Total_Price=row[30]
            rowTostore.Payment_Method=row[31]
            rowTostore.Sale_Date=row[32]
            #rowTostore.Checkout_Date
            rowTostore.Paid_on_Date=row[33]
            rowTostore.Dispatch_Date_=row[37]
            #rowTostore.Invoice_date
            #rowTostore.Invoice_number
            rowTostore.Feedback_left=row[38]
            rowTostore.Feedback_received=row[39]
            rowTostore.Notes_to_yourself=row[40]
            #rowTostore.Unique_Product_Id
            #rowTostore.Private_Field
            #rowTostore.ProductIDType
            #rowTostore.ProductIDValue
            #rowTostore.ProductIDValue2
            rowTostore.PayPal_Transaction_ID=row[41]
            rowTostore.Delivery_Service=row[42]
            #rowTostore.Cash_on_delivery_option
            rowTostore.Transaction_ID=row[44]
            rowTostore.Order_ID=row[1]
            rowTostore.Variation_Details=row[45]
            rowTostore.Global_Shipping_Programme=row[46]
            rowTostore.Global_Shipping_Reference_ID=row[47]
            rowTostore.Click_and_Collect=row[48]
            rowTostore.Click_and_Collect_Reference=row[49]
            rowTostore.Post_To_Address_1=row[14]
            rowTostore.Post_To_Address_2=row[15]
            rowTostore.Post_To_City=row[16]
            rowTostore.Post_To_County=row[17]
            rowTostore.Post_To_Postcode=row[18]
            rowTostore.Post_To_Country=row[19]
            rowTostore.eBay_Plus=row[50]
            classArray.append(rowTostore)
            
    
    print("salida")
    writeFile("Bad1_fixed.csv",classArray)       


def writeFile(fileToWrite,classArray):
    with open(fileToWrite, 'w') as fileToSave:
        writer = csv.writer(fileToSave,quoting=csv.QUOTE_ALL)
        writer.writerow(['Sales Record Number', 'User Id', 'Buyer Full name', 'Buyer Phone Number', 'Buyer Email', 'Buyer Address 1', 'Buyer Address 2', 'Buyer Town/City', 'Buyer County', 'Buyer Postcode', 'Buyer Country', 'Item Number', 'Item Title', 'Custom Label', 'Quantity', 'Sale Price', 'Included VAT Rate', 'Postage and Packaging', 'Insurance', 'Cash on delivery fee', 'Total Price', 'Payment Method', 'Sale Date', 'Checkout Date', 'Paid on Date', 'Dispatch Date ', 'Invoice date', 'Invoice number', 'Feedback left',
                         'Feedback received', 'Notes to yourself', 'Unique Product Id', 'Private Field', 'ProductIDType', 'ProductIDValue', 'ProductIDValue-2', 'PayPal Transaction ID', 'Delivery Service', 'Cash on delivery option', 'Transaction ID', 'Order ID', 'Variation Details', 'Global Shipping Programme', 'Global Shipping Reference ID', 'Click and Collect', 'Click and Collect Reference #', 'Post To Address 1', 'Post To Address 2', 'Post To City', 'Post To County', 'Post To Postcode', 'Post To Country', 'eBay Plus'])

        for rowClass in classArray:
            writer.writerow([rowClass.Sales_Record_Number, rowClass.User_Id,rowClass.Buyer_Full_name,rowClass.Buyer_Phone_Number,rowClass.Buyer_Email,rowClass.Buyer_Address_1,rowClass.Buyer_Address_2,rowClass.Buyer_TownCity,rowClass.Buyer_County,rowClass.Buyer_Postcode,rowClass.Buyer_Country,rowClass.Item_Number,rowClass.Item_Title,rowClass.Custom_Label,rowClass.Quantity,rowClass.Sale_Price,rowClass.Included_VAT_Rate,rowClass.Postage_and_Packaging,rowClass.Insurance,rowClass.Cash_on_delivery_fee,rowClass.Total_Price,rowClass.Payment_Method,rowClass.Sale_Date,rowClass.Checkout_Date,rowClass.Paid_on_Date,rowClass.Dispatch_Date_,rowClass.Invoice_date,rowClass.Invoice_number,rowClass.Feedback_left,rowClass.Feedback_received,rowClass.Notes_to_yourself,rowClass.Unique_Product_Id,rowClass.Private_Field,rowClass.ProductIDType,rowClass.ProductIDValue,rowClass.ProductIDValue2,rowClass.PayPal_Transaction_ID,rowClass.Delivery_Service,rowClass.Cash_on_delivery_option,rowClass.Transaction_ID,rowClass.Order_ID,rowClass.Variation_Details,rowClass.Global_Shipping_Programme,rowClass.Global_Shipping_Reference_ID,rowClass.Click_and_Collect,rowClass.Click_and_Collect_Reference,rowClass.Post_To_Address_1,rowClass.Post_To_Address_2,rowClass.Post_To_City,rowClass.Post_To_County,rowClass.Post_To_Postcode,rowClass.Post_To_Country,rowClass.eBay_Plus])

if __name__ == '__main__':
    readcsv("Bad1.csv")
