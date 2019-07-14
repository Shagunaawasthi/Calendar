from datetime import datetime, timedelta,date
from calendar import HTMLCalendar
from .models import Event,Detail
from cal.forms import EventForm
from django.utils.dateparse import parse_datetime
from datetime import timezone
import calendar
from pandas.tseries import offsets


import pytz

class Calendar(HTMLCalendar):
	
	def __init__(self, request,year=None, month=None):
		self.year = year
		self.month = month
		self.request=request
		super(Calendar, self).__init__()
#cee1f3
	# formats a day as a td
	# filter events by day
	def formatday(self, day, events, m):
		#global counter
		
		if day != 0:
			dt_str=str(self.year)+' '+str(m)+' '+str(day)
			dt=datetime.strptime(dt_str,'%Y %m %d').replace(tzinfo=timezone.utc)
			
	#		#print(dt)
#
		AP_class=""
		eventFlag=False
		Salaryflag=False
		ram=""
		Payrollflag=False
		h=""
		sal=""
		sal_day=""
	#	x=''
	#	a=''
	#	y=''
	#	z=''
	#	l=''
	#	j=''
	#	k=''
	#	
	#	n=''
	#	date=''
	#	ram=""
	#	AP_class=""
	#	
#
	#	
#
	#	j={self.month}
	#	
	#	k=({self.year})
	#	l={day}
	#	v=set(map(str,j))
	#	o=set(map(str,k))
	#	n=set(map(str,l))
	#	q=''.join(v)
	#	p=''.join(o)
	#	temp=""
	#	w=''.join(n)
    #	
	#	#n=j+k+l
	#	if len(q)==1:
	#		temp= '0'+q
	#	if len(q)==2:
	#		temp= q
	#	date=p+'-'+temp+'-'+w
	#	#print(type(date))
	#	
  #
	#	#AP_event = events.filter(title__iexact='AP')
	#	#print(AP_event)
	#	#
	#	#for event in AP_event:
	#	#	print(event.start_time)
	#	#	
	#	#	if event.title == "AP":
	#	#		#print("yoho")
##
	#	#		AP_class=" AP"
	#	#	else:
	#	#		AP_class=""	
	#	#		#print ("holo")
		
		
		#y=self.year-2019
		#if y%5==0:
		#	AP_str=str(self.year)+' '+str(1)+' '+str(1)
		#	
		#	AP_start=datetime.strptime(AP_str,'%Y %m %d').replace(tzinfo=timezone.utc)
		#else:
		#	AP_start_temp= "2019-01-01"
		#	AP_start= datetime.strptime(AP_start_temp,'%Y-%m-%d').replace(tzinfo=timezone.utc)
		
		temp_str=str(self.year)+' '+str(1)+' '+str(1)
		temp=datetime.strptime(temp_str,'%Y %m %d').replace(tzinfo=timezone.utc)
		adj = (0 - temp.weekday()) % 7
		temp += timedelta(days=adj)
		temp+= timedelta(weeks=3)
		
		

		
		if day!=0:
			#compare = datetime.strptime( "2019-01-01" ,'%Y-%m-%d').replace(tzinfo=timezone.utc)
			#recheck_str=str(self.year)+' '+str(1)+' '+str(1)
			#recheck=datetime.strptime(recheck_str,'%Y %m %d').replace(tzinfo=timezone.utc)
			#if AP_start == compare:
			#	print("y")
			#print(dt)
			#print(dt - AP_start + timedelta(1))
			
			dys = (dt - temp )
			
			
			
			#else:
			#	print("n")
			#	dys = (dt - AP_start )
				
			dts = (dys).days
			count=""

			if dts<=0:
				count="AP-1"
				
			if 0<dts<=28:
				count="AP-2"
			if 28<dts<=56:
				
				count="AP-3"
			if 56<dts<=84:
				
				count="AP-4"
			if 84<dts<=112:
				count="AP-5"
				
			if 112<dts<=140:
				count="AP-6"
				
			if 140<dts<=168:
				count="AP-7"
				
			if 168<dts<=196:
				count="AP-8"
				
			if 196<dts<=224:
				count="AP-9"
				
			if 224<dts<=252:
				count="AP-10"
				
			if 252<dts<=280:
				count="AP-11"
				
			if 280<dts<=308:
				count="AP-12"
				
			if 308<dts<=336:
				count="AP-13"
			
			

			#print(dt)
			#print(dts)
			
			
			if dts>=0:
				
				if dts%28==0:
					Payrollflag=True
					if dts%336==0 and dts!=0:
						test2=dt + timedelta(days=7)
						if test2.year == self.year:
							Payrollflag=False
					#else:
						
							
						#dys2 = (test2 - temp ).days
					
					#if dys2%343!=0:
					#Payrollflag=True
						#print('pflag')
				if dts%343==0:
					
					test=dt - timedelta(days=7)
					dys1 = (test - temp ).days
					if dys1%28==0:
						Payrollflag=True  
						#self.request.session['counter']=1
					#print(dts)
					#print(dt)
					#test=dt + timedelta(days=7)
					#print(test)
					#print(type(test.year))
					#print(type(self.year))
					#if test.year == self.year:
					#	print("hi")
					#	Payrollflag=True  

				
						#self.request.session['counter']=1
									
					#print(dts)
					#print(dt)
					#test=dt + timedelta(days=7)
					#print(test)
					#print(type(test.year))
					#print(type(self.year))
					#if test.year == self.year:
					#	print("hi")
					#	Payrollflag=True  
					#print(dt)
					#ap=ap+1
					#if ap==13:
					#	ap=1
					#	test=(dt + timedelta(days=7)).year

					
					
					
						
				
						
						#self.request.session['counter']=1
				#if dt != recheck:
					
				
						

				
				
					
				#sat=(dt  + timedelta(days=3))
				#sal= datetime.strftime(sat,"%d")
				
			#if day==sal:
			#	print(day)
			#else:
			#	print("m")	
				
				
				
				
				
				
			
			
		
			
		
			#if dys%28 == 0:
			#	Payrollflag=True

				
		
			
			
			#AP_start = next_start
		
		
	#	next_start= AP_start +  timedelta(days=28) 
#
	#	AP_event = next_start - timedelta(days=1)
#
	#	
	#	AP_start = next_start
	#	print(m)
	#	print(next_start)
	#	print(AP_event)
	
	
		
			
			month_end= calendar.monthrange(self.year,m)[1]
		
	
				
			if day !=0 and Payrollflag:
				
				
				sal = dt + timedelta(days=3)
				#if 'day_id' not in self.request.session:
				self.request.session['day_id']=sal.day
				self.request.session['counter']=sal.month
			
				
				
		#		print(self.request.session['day_id'])
		#		print(self.request.session['counter'])
		#		sal_day = sal.day #int(datetime.strftime(sal,"%d"))
		#		#print(sal_day)
		#	else:
		#		sal_day = 0	
		#		
			

		#
			
				
		#print(type(salary_closing))
		month_events=events.filter(start_time__month=m)
		
		events_per_day = month_events.filter(start_time__day = day )
	
		
		#for event in events_per_day:
		#	title_of_event = event.title
			

		#	if title_of_event=="AP": 
				
		#		AP_class=" AP"
		#		flag=True
				
				
		#	else:
		#		AP_class=""
		for et in events:
			casual_start_time=et.start_time
			casual_end_time= et.end_time
			casual_title = et.title
			 
			

			if day!=0 and et.title!="Ramadaan" and casual_start_time<=dt and dt<=casual_end_time:
				eventFlag=True
			
			
		Ramadaan_event= events.filter(title__iexact='Ramadaan')
		
		
		#print(Ramadaan_event)
		
		#if w[0] == '0':
			#z=datetime.strptime('5555-01-01','%Y-%m-%d').replace(tzinfo=timezone.utc)
		#else:
			#z=datetime.strptime(date,'%Y-%m-%d').replace(tzinfo=timezone.utc)
				#print(z)

		#if Ramadaan_event.count() != 0:
			#print("Ram")
			#print(z)
		#k=0
#
		#k=k+1
		##print(k)
#
		for event in Ramadaan_event:
			
			x=event.start_time
			
			
			
			#z= datetime.strptime(date,'%Y-%m-%d')
			
#
			y= event.end_time
			z= event.title
			

				
			
		#	
		#	
#
		#	if w[0] == '0':
		#		z=datetime.strptime('5555-01-01','%Y-%m-%d').replace(tzinfo=timezone.utc)
		#	else:
		#		z=datetime.strptime(date,'%Y-%m-%d').replace(tzinfo=timezone.utc)
				
		
		#
		#	#print("x=")
		#	#print(x)
			#print("y=")
			#print(y)
			#print("z=")
			
			#if m<int(datetime.strftime(y,'%m')):
					#print(z)
					#print(m)
					#print(int(datetime.strftime(y,'%m')))
				
				
				#while m<int(datetime.strftime(y,'%m')):
					
						#print("yoho")
						#print("lies between")
			#			ram=" please"
			if day!=0 and x<=dt and dt<=y:
			
				ram=" please"
					

				
					
				
				
			#		elif m==int(datetime.strftime(y,'%m')):
			#			new_month= m+1
			#			temp =p+'-'+'0'+new_month+'-'+w
			#			print(temp)
			#			break
			#			#x=datetime.strptime(date,'%Y-%m-%d').replace(tzinfo=timezone.utc)
							
								
			else:
				ram=""
							#print(z)
							#print("lies outside")
	    	    #	x=day + m+1 + year
				#	 if(x<=z and z<=y):
				#			#print("lies between")
				#			ram=" please"
				#			#print("yoho")
				#		else:
				#			ram=""
				#			#print(z)
				#			#print("lies outside")
			#else:
			#		print("huh")
				#	if(x<=z and z<=y):
				#			#print("lies between")
				#			ram=" please"
				#			#print("yoho")
				#		else:
				#			ram=""
				#			#print(z)
				#			#print("lies outside")
#	
		


		

 


			 
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'
			
			
			

		#f5faff;

		if day != 0:

			
			#print(dt)	
			#print(day)
			#print(sal_day)
			#print(day)
			c = "date " + ram 
			if day==month_end:
				c = "date last" 
			if Payrollflag:
				c="date payroll"
			if 'day_id' in self.request.session:
				if    dt.day==self.request.session['day_id'] and  dt.month==self.request.session['counter']   : 
			
					c= "date salary"
			
			if len(d)>0:
				c = "date ok" + ram  
			
			if eventFlag:
				c = "date ok"
			
			self.month = m
			
			return f'<td ><div class="{c}"><span><a   href="event/list/?day={day}&month={self.month}&year={self.year}" title={ count }>{day}</a> </span> </div > <ul class="hide" > {d} </ul></td>'
			
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events, m): 
		
		
		week = ''

		
	
		for day, weekday in theweek:
			
			week  += self.formatday(day, events, m)

		
				
				   

		return f'<tr > {week} </tr>'

	def formatmonth(self,m,events,withyear= True):
		month = ''

		#events = Event.objects.filter(start_time__year=self.year, start_time__month=m)
		
		
		#print(events)
		#print(self.year)
		
	   
		month = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar" style="min-height:200px">\n'
		month += f'{self.formatmonthname(self.year,m, withyear=withyear)}\n'
		month += f'{self.formatweekheader()}'
		w=0
		for week in self.monthdays2calendar(self.year, m):
			w+=1
			month += f'{self.formatweek(week, events, m)}\n'
		wk=6-w
		for i in range(0,wk):
			
			month += f'<tr ><td>&nbsp</td></tr>\n'

		return  month

	def formatyear(self,theyear):
		cal = ''
		

		events = Event.objects.filter(start_time__year=self.year)
		
		for i in range(1,13):
			#events_of_month=events.filter(start_time__month=i)

			
			#for i in range(1,13):


			cal += self.formatmonth(i,events,withyear=True)
			
		return cal 