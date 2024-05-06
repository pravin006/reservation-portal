from models.users import User
from app import db
from datetime import datetime, timedelta

class CHART(db.Document):  
    
    meta = {'collection': 'chart'}
    # data required to plot the graph
    charts = db.DictField()
    # hole on graph
    labels = db.DictField()
    


    # def new_collection(self, timing, index, par, dist):
    #     lb = ['Start time']
    #     for i in range(len(par)):
    #         lb.append(f'Hole {i+1}')
    #     lb.reverse()
        
    #     self.update(__raw__={'$set': {'labels': lb}})

        
    #     readings = {}
    #     for t in range(len(timing)):
    #         setup = 0
    #         play = 0
    #         starttime = timing[t]
            
    #         readings[f'Flight {t+1}'] = [starttime]

    #         for n in range(len(index)):
    #             if index[n] <= 6:
    #               setup = par[n] * 180
    #             elif index[n] <= 12:
    #               setup = par[n] * 150
    #             elif index[n] <= 18:
    #               setup = par[n] * 120
                
    #             if dist[n] <= 100:
    #                 play = 60
    #             elif dist[n] <= 200:
    #                 play = 120
    #             elif dist[n] <= 300:
    #                 play = 180
    #             elif dist[n] <= 400:
    #                 play = 240
    #             elif dist[n] <= 500:
    #                 play = 300
    #             elif dist[n] > 500:
    #                 play = 360

    #             delta = timedelta(seconds=play+setup)
    #             starttime += delta

    #             if readings.get(f'Flight {t+1}'):
    #                 readings[f'Flight {t+1}'].append(starttime) 
                
    #     for k in readings.keys():
    #         readings[k].reverse()
            
           
    #     self.update(__raw__={'$set': {'charts': readings}})

    def new_collection(self, timing, holes):
        lb = ['Start time']
        for i in range(len(holes)):
            lb.append(f'Hole {i+1}')
        lb.reverse()
        
        self.update(__raw__={'$set': {'labels': lb}})

        
        readings = {}
        for t in range(len(timing)):
            setup = 0
            play = 0
            starttime = timing[t]
            
            readings[f'Flight {t+1}'] = [starttime]

            for n in range(len(holes)):
                if holes[n].index <= 6:
                  setup = holes[n].par * 180
                elif holes[n].index <= 12:
                  setup = holes[n].par * 150
                elif holes[n].index <= 18:
                  setup = holes[n].par * 120

                if holes[n].dist <= 100:
                    play = 60
                elif holes[n].dist <= 200:
                    play = 120
                elif holes[n].dist <= 300:
                    play = 180
                elif holes[n].dist <= 400:
                    play = 240
                elif holes[n].dist <= 500:
                    play = 300
                elif holes[n].dist > 500:
                    play = 360

                delta = timedelta(seconds=play+setup)
                starttime += delta

                if readings.get(f'Flight {t+1}'):
                    readings[f'Flight {t+1}'].append(starttime)

        for k in readings.keys():
            readings[k].reverse()
            
           
        self.update(__raw__={'$set': {'charts': readings}})