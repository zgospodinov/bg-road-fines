import email_sender
from road_fines import get_road_fines


def main():
    print("Hello from bg-road-fines!")
    road_fines_result = get_road_fines()
    
    # road_fines_result = None
    if(road_fines_result):
        email_sender.send_email(
        subject="Обобщена проверка на задължения по фиш, НП или споразумение",
        body=road_fines_result)
    else:
        pass

if __name__ == "__main__":
    main()
