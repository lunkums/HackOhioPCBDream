using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using UnityEngine;

public class DataPopulator : MonoBehaviour
{
    public static DataPopulator Instance { get; private set; }

    [SerializeField] private TextAsset csvFile;
    [SerializeField] private Gradient gradient;

    private Dictionary<(DateTime dateTime, string columnName), float> data
        = new Dictionary<(DateTime dateTime, string columnName), float>();
    private DateTime currentTime;

    private float maxData;

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

        string[] columnNames = CSVParser.Split(lines[0]);

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
            string[] columns = line.Split(',');

            DateTime.TryParse(columns[0], out currentTime);
            for (int j = 1; j < columns.Length; j++)
            {
                data.Add((currentTime, columnNames[j]), float.TryParse(columns[j], out float result) ? result : 0);
                maxData = Math.Max(maxData, result);
            }
        }
    }

    public float GetData(string buildingName)
    {
        return data[(currentTime, buildingName)];
    }

    public Color GetColorFromData(float data)
    {
        return gradient.Evaluate(data / maxData);
    }

}
