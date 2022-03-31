month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions.get("hello"))
print(month_conversions.get("hello", "Not a valid key!"))