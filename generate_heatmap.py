
import datetime as dt
from email import utils
from subprocess import check_output

def main():

	today = dt.datetime.now().astimezone()
	start = dt.datetime(today.year, today.month, today.day).astimezone()
	current = start

	# Clear file
	print('Clearing "data.txt"')
	open('data.txt', 'w').close()

	# Initial commit
	print('Initial "data.txt" commit')
	check_output('git add data.txt', shell=True).decode()
	check_output('git commit -m "Initial commit"', shell=True).decode()

	# Create dummy commits
	print('Creating commits in "data.txt"...')
	for i in range(4*24 + 1):

		print(f'Commit and push datetime: {current}')

		with open('data.txt', 'a') as data:
			data.write(utils.format_datetime(current)+'\n')
		
		cmd = f'git commit --date="{utils.format_datetime(current)}" -m "Add {current.strftime("%Y-%m-%d %H:%M")} to data.txt" data.txt'

		check_output(cmd, shell=True).decode()
		check_output('git push', shell=True).decode()
		
		current += dt.timedelta(minutes=15)

	# Update actions to seem as if they were pushed eveyr 15 mins
	with open('update_action.sql', 'w') as sql:
		rows = 97
		step = 15 * 60
		ts = int(start.timestamp())
		print(f'Writing updates to "update_action.sql" to last {rows} entries with starting timestamp: {ts}')

		#for i in range(1, rows+1):
		for i in range(rows-1, -1, -1):
			sql.write(f'UPDATE action SET created_unix={ts} WHERE id=(SELECT MAX(id)-{i} FROM action);\n')
			ts += step

if __name__ == '__main__':
	main()