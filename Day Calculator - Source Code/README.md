# DAY CALCULATOR BY BRACISTONE STUDIOS

## About the Calculator

Day Calculator is an application software developed by Bracistone Studios. Its purpose is to determine the day of the week corresponding to any given date within the range of **1 January 1 CE to 31 December 10000 CE**, inclusive.

The calculator is developed using Python without relying on any external libraries. However, Tkinter, a standard Python library, is used in the final version, primarily for the graphical user interface (GUI).

The calculator accepts dates within the specified range according to the **Proleptic Gregorian Calendar**. Instead of processing dates using Python's date-handling facilities, it represents each date using integers and uses **20 July 2026** as its reference date.

It then uses mathematical reasoning to calculate the number of days between the given date and the reference date. Using this difference, it determines the corresponding day of the week.

For example, if the user enters **1 January 2027**, the calculator returns **Friday**.

**Note on Historical Dates:** Although the calculator produces mathematically consistent results according to the Proleptic Gregorian Calendar, its results for historical dates may differ from historical records. This is because the Gregorian Calendar was introduced by Pope Gregory XIII in 1582, and its adoption occurred gradually across different countries over several centuries. Earlier dates are calculated by extending Gregorian calendar rules backwards, rather than following the calendar systems actually used at the time.

## Version and Updates

The source code of Day Calculator was released on **1 November 2026**. Although complete and fully functional, this release does not represent the full version of the application. It does not contain any GUI elements and can therefore only be executed through a terminal.

Despite this difference in interface, the source-code release and the full application share fundamentally the same underlying functionality and calculation logic.

To get the full version, visit: https://bracistone-studios.itch.io/day-calculator

The released source code will not receive any further updates. However, the full application may receive occasional GUI updates.

## License

Day Calculator is distributed under the **MIT License**, a permissive open-source license. The complete license terms can be found in the 'LICENSE.md' file in this repository.

In short, the license permits users to use, copy, modify, publish, distribute, sublicense, and sell copies of the software, subject to the conditions stated in the license. It also permits integration of this software into other software.

**Thank You!**

Regards,  
**Syed Azfar**  
Developer, Bracistone Studios
