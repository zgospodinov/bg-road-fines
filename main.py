from email_sender import EmailSender
from road_fines import get_road_fines


def main():    
    print("Hello from bg-road-fines!")
    
    email_service = EmailSender()
    road_fines_result = get_road_fines()
    
    if(road_fines_result):
        email_service.send_email(body=road_fines_result)
    else:
        email_service.send_error_email(message=road_fines_result)

if __name__ == "__main__":
    main()
