import logging
import azure.functions as func
from .main import main as run_bg_road_fines_check

app = func.FunctionApp()

@app.timer_trigger(
        schedule="0 0 9 * * 1,4", 
        arg_name="myTimer", 
        run_on_startup=False,
        use_monitor=False) 
def check_fines(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info("Police ticket checker function started.")
    run_bg_road_fines_check()

    logging.info("Police ticket checker function completed.")