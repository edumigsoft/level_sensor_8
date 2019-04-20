# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#import app

#webrepl.start()
#app = app.APP()
#app.main()
gc.collect()
