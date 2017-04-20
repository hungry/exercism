package twelve

const testVersion = 1

func Song() string {
	song := ""
	for day := 1; day <= 12; day++ {
		song += Verse(day) + "\n"
	}
	return song
}

func Verse(day int) string {
	day--

	verse := "On the " + gifts[day].day +
		" day of Christmas my true love gave to me, " +
		gifts[day].gift

	if day > 0 {
		for previousDay := day - 1; previousDay > 0; previousDay-- {
			verse += ", " + gifts[previousDay].gift
		}
		verse += ", and " + gifts[0].gift
	}

	return verse + "."
}

type gift struct {
	day, gift string
}

var gifts = []gift{
	{"first", "a Partridge in a Pear Tree"},
	{"second", "two Turtle Doves"},
	{"third", "three French Hens"},
	{"fourth", "four Calling Birds"},
	{"fifth", "five Gold Rings"},
	{"sixth", "six Geese-a-Laying"},
	{"seventh", "seven Swans-a-Swimming"},
	{"eighth", "eight Maids-a-Milking"},
	{"ninth", "nine Ladies Dancing"},
	{"tenth", "ten Lords-a-Leaping"},
	{"eleventh", "eleven Pipers Piping"},
	{"twelfth", "twelve Drummers Drumming"},
}
