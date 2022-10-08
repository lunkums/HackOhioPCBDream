using cakeslice;
using System.Collections.Generic;
using UnityEngine;

public class BuildingManager : MonoBehaviour
{
    public static BuildingManager Instance { get; private set; }

    [SerializeField] private float maxBuildingHeight;

    private List<Building> buildings = new List<Building>();

    public float MaxBuildingHeight => maxBuildingHeight;

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

        foreach (Building building in gameObject.GetComponentsInChildren<Building>())
        {
            buildings.Add(building);
            building.gameObject.AddComponent<Outline>();
        }
    }

    public void ReadjustBuildings()
    {
        foreach (Building building in buildings)
        {
            building.Adjust();
        }
    }
}
