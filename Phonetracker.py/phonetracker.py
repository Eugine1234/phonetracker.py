import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse('')
phone_number1 = phonenumbers.parse('')
phone_number1 = phonenumbers.parse('')
phone_number1 = phonenumbers.parse('')



print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number1,"en"));