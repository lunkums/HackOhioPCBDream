using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using UnityEngine;

public class DataManager : MonoBehaviour
{
    public static DataManager Instance { get; private set; }

    [SerializeField] private TextAsset csvFile;
    [SerializeField] private Gradient gradient;

    private Dictionary<DateTime, string> data = new Dictionary<DateTime, string>();

    private DateTime[] dateTimes;
    private float[] dataColumns;
    private string[] columnNames;
    private float currentMax;

    private int dateTimeIndex;
    private DataType dataType;

    public int NumOfDateTimes => dateTimes.Length - 1;
    public DateTime Now => dateTimes[dateTimeIndex];
    public int DateTimeIndex
    {
        set
        {
            dateTimeIndex = value;
            ReloadColumn();
        }
    }
    public DataType CurrentDataType
    {
        set
        {
            dataType = value;
            ReloadColumn();
        }
    }

    public enum DataType
    {
        ChilledWater,
        Electricity,
        HotWater,
        NaturalGas,
        Steam,
        Total
    }

    private string DataTypeAsString
    {
        get
        {
            switch (dataType)
            {
                case DataType.ChilledWater:
                    return "Chilled Water Consumption";
                case DataType.Electricity:
                    return "Electricity Consumption";
                case DataType.HotWater:
                    return "Hot Water Consumption";
                case DataType.NaturalGas:
                    return "Natural Gas Consumption";
                case DataType.Steam:
                    return "Steam Consumption";
                case DataType.Total:
                    return "Total Energy Consumption (Cleaned)";
                default:
                    return "";
            }
        }
    }

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(this);
        }
        else
        {
            Instance = this;
        }

        Regex CSVParser = new Regex(",(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))");

        string text = csvFile.text;
        string[] lines = text.Split("\n");
        dateTimes = new DateTime[lines.Length - 2];
        columnNames = CSVParser.Split(lines[0]);
        dataColumns = new float[columnNames.Length];

        for (int i = 0; i < columnNames.Length; i++)
        {
            columnNames[i] = columnNames[i].Replace("\"", "");
            Debug.Log(columnNames[i]);
        }

        // Ignore the last line of the CSV file; garbage
        int length = lines.Length - 1;
        for (int i = 1; i < length; i++)
        {
            string line = lines[i];

            DateTime.TryParse(line.Substring(0, line.IndexOf(',')), out DateTime currentTime);
            dateTimes[i - 1] = currentTime;
            data.Add(currentTime, line);
        }

        CurrentDataType = DataType.Total;
        DateTimeIndex = 1;
    }

    public float GetData(string buildingName)
    {
        string columnName = $"{buildingName} - {DataTypeAsString} (kBTU)";

        // Ignore first column name "Series Name"
        for (int i = 1; i < columnNames.Length; i++)
        {
            if (!columnName.Equals(columnNames[i]))
                continue;

            return dataColumns[i];
        }
        return -1;
    }

    public Color GetColorFromData(float data)
    {
        return gradient.Evaluate(GetRatio(data));
    }

    public float GetRatio(float data)
    {
        return data / currentMax;
    }

    private void ReloadColumn()
    {
        string[] columns = data[Now].Split(',');
        // Reset the current max to 1 to avoid divide by 0 errors
        currentMax = 1;

        // Ignore first column "Date Time"
        for (int i = 1; i < columns.Length; i++)
        {
            float curr = float.TryParse(columns[i], out float result) ? result : 0;
            dataColumns[i] = curr;
            if (columnNames[i].Contains(DataTypeAsString))
                currentMax = Math.Max(curr, currentMax);
        }
    }
}
